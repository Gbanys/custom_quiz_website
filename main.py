from pathlib import Path
from typing import Optional
from fastapi.responses import RedirectResponse
import uvicorn
from fastapi import FastAPI, HTTPException, Request, WebSocket
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from datetime import datetime
import time
import os

from database.database import get_all_answers, get_answers_from_question, get_first_unanswered_question, get_questions_from_quiz, get_quizzes_from_user, get_single_quiz, reset_all_questions_from_quiz, update_question_status

app = FastAPI()

app.mount(
    "/static",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "custom_quiz_website" / "app" / "src" / "static"),
    name="static",
)

BASE_DIR = Path(__file__).resolve().parent / "app" / "src"

templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))

USER_ID = 1

@app.get("/")
async def return_home_page(request: Request):
    return templates.TemplateResponse(
        "home.html",
        context={
            "request": request,
            "zip": zip
        }
    )

@app.get("/quiz_menu/{quiz_type}")
async def return_quiz_menu_page(request: Request, quiz_type: str):
    quizzes = get_quizzes_from_user(user_id=USER_ID)
    filtered_quizzes = [quiz for quiz in quizzes if quiz_type in quiz[1]]
    return templates.TemplateResponse(
        "quiz_menu.html",
        context={
            "request": request,
            "zip": zip,
            "quizzes" : filtered_quizzes,
            "quiz_type" : quiz_type
        }
    )


@app.get("/quiz/reset/{user_id}/{quiz_id}/{quiz_type}")
async def reset_quiz(request: Request, user_id, quiz_id, quiz_type):
    reset_all_questions_from_quiz(quiz_id)
    return RedirectResponse(f"/quiz/{user_id}/{quiz_id}/{quiz_type}")

@app.get("/quiz/{user_id}/{quiz_id}/{quiz_type}")
async def return_quiz_page(request: Request, user_id: int, quiz_id: int, quiz_type: str):
    quiz = get_single_quiz(quiz_id=quiz_id)

    try:
        first_unanswered_question = get_first_unanswered_question(quiz_id=quiz_id)
        question_id = first_unanswered_question[0][0]
    except IndexError:
        questions = get_questions_from_quiz(quiz_id=quiz_id)
        number_of_questions_answered_correctly = len([question for question in questions if question[2] == 1])
        pass_rate = quiz[0][3]
        return templates.TemplateResponse(
        "quiz.html",
        context={
            "request" : request,
            "zip" : zip,
            "quiz_id" : quiz_id,
            "user_id" : user_id,
            "quiz_name" : quiz[0][1],
            "quiz_inprogress" : False,
            "quiz_type" : quiz_type,
            "number_of_questions_answered_correctly" : number_of_questions_answered_correctly,
            "total_number_of_questions" : len(questions),
            "pass_rate" : pass_rate
        }
    )

    answers = get_answers_from_question(question_id=question_id)
    return templates.TemplateResponse(
        "quiz.html",
        context={
            "request" : request,
            "zip" : zip,
            "quiz_id" : quiz_id,
            "question_id" : question_id,
            "question_name" : first_unanswered_question[0][1],
            "quiz_name" : quiz[0][1],
            "quiz_type" : quiz_type,
            "answers" : answers,
            "quiz_inprogress" : True
        }
    )

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        if data['status'] == 'update_question':
            await check_if_user_is_correct(int(data['question_id']), data['answer_ids'], websocket)

async def check_if_user_is_correct(question_id, chosen_answer_ids, websocket):
    if not chosen_answer_ids:
        await websocket.send_json(
        {
            "type" : "do_nothing",
        }
    )
    else:
        answers = get_answers_from_question(question_id=question_id)
        correct_answer_ids = [str(answer[0]) for answer in answers if answer[2] == True]
        wrong_chosen_answer_ids = []
        correct_chosen_answer_ids = []
        for chosen_answer_id in chosen_answer_ids:
            if chosen_answer_id in correct_answer_ids:
                correct_chosen_answer_ids.append(chosen_answer_id)
            else:
                wrong_chosen_answer_ids.append(chosen_answer_id)

        if not wrong_chosen_answer_ids:
            update_question_status(question_id=question_id, answered_correctly=True)
        else:
            update_question_status(question_id=question_id, answered_correctly=False)

        await websocket.send_json(
            {
                "type" : "submit_answer",
                "correct_answer_ids" : correct_answer_ids,
                "wrong_chosen_answer_ids" : wrong_chosen_answer_ids
            }
        )

async def update_quiz_question(question_id: int, answered_correctly: bool):
    update_quiz_question(question_id=question_id, answered_correctly=answered_correctly)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)