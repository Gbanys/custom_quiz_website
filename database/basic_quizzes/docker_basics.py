from database.database import add_answer_to_question, add_question_to_quiz, add_quiz_to_user, get_latest_question_id_from_quiz, get_latest_quiz_id_from_user

def create_docker_basics_quiz(user_id: int):
    add_quiz_to_user(name="Docker Basics", ongoing=False, pass_rate=70, user_id=user_id)
    quiz_id = get_latest_quiz_id_from_user(user_id=user_id)[0][0]

    # 1
    add_question_to_quiz(question="Which of the following are the only officially supported distributions for Docker hosts? (Select TWO)", quiz_id=quiz_id)
    latest_id = get_latest_question_id_from_quiz(quiz_id=quiz_id)[0][0]
    add_answer_to_question(answer="Linux Mint", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="CentOS", is_correct=True, question_id=latest_id)
    add_answer_to_question(answer="Red Hat", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="OpenSUSE", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="Debian", is_correct=True, question_id=latest_id)

    # 2
    add_question_to_quiz(question="A developer is running a docker container named 'bob_container'. He would like the see the OS version that the container is using.\
What can he do?", quiz_id=quiz_id)
    latest_id = get_latest_question_id_from_quiz(quiz_id=quiz_id)[0][0]
    add_answer_to_question(answer="Run the 'docker container bob_container show os' command", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="Run the 'docker exec bob_container cat etc/hosts' command."
    , is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="Run the 'docker exec bob_container cat etc/*release*' command", is_correct=True, question_id=latest_id)
    add_answer_to_question(answer="There is nothing he can do. Once you run the docker container you can't check the OS being used." , is_correct=False, question_id=latest_id)

    # 3
    add_question_to_quiz(question="A developer is trying to run a python script inside a container. The container seems to be running at first, however after 5 seconds he realises that the container \
is no longer running. What is the reason for this?", quiz_id=quiz_id)
    latest_id = get_latest_question_id_from_quiz(quiz_id=quiz_id)[0][0]
    add_answer_to_question(answer="The python script has finished executing after 5 seconds. The container only runs as long as the process itself.", is_correct=True, question_id=latest_id)
    add_answer_to_question(answer="There was a problem when building the image. Most likely, there's an issue with the Dockerfile.", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="The developer used the wrong command to run the container. He should've used -d to run the container in the background.", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="The developer is using an old docker version to run the container.", is_correct=False, question_id=latest_id)
    
    # 4
    add_question_to_quiz(question="You would like to run a container which uses the latest version of the nginx image. Which of the following commands will achieve this?", quiz_id=quiz_id)
    latest_id = get_latest_question_id_from_quiz(quiz_id=quiz_id)[0][0]
    add_answer_to_question(answer="docker run --version latest nginx", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="docker run --version=latest nginx", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="docker run nginx latest", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="docker run nginx", is_correct=True, question_id=latest_id)

    # 5
    add_question_to_quiz(question="Donald is working on a MySQL database and he wants to run the mysql database inside a docker container. He is able to successfully run this database however \
by some accident the database docker container has been removed. Donald investigates the issue and decides to run the container again, however, whilst looking \
at the database tables, he realizes that all of the data has been lost and he needs to add the same entries to the table again. \
What is the best way to prevent this data loss from occuring if this container is removed again?", quiz_id=quiz_id)
    latest_id = get_latest_question_id_from_quiz(quiz_id=quiz_id)[0][0]
    add_answer_to_question(answer="Nothing. The database contents can only live inside the container volume which always exists on the same directory..", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="He can copy all of the database contents from the container onto the host machine. If the container is recreated he can copy these contents from the host machine \
    and paste it into the container again.", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="He can create a volume mapping by creating a new folder on the host machine and mounting it onto a directory inside the docker container. All of the database contents will be \
    persisted in this new directory created on the host machine.", is_correct=True, question_id=latest_id)
    add_answer_to_question(answer="He can move the files from the docker volume directory into a different directory inside the container called /var/lib/persistent. Edit the docker configuration files \
    so that the docker container is reading the files from this directory instead.", is_correct=False, question_id=latest_id)

    # 6
    add_question_to_quiz(question="Alice is inspecting her environment. She wants to see all the docker images that are available already. Which commands can she use to view all the docker images? (Select TWO)", quiz_id=quiz_id)
    latest_id = get_latest_question_id_from_quiz(quiz_id=quiz_id)[0][0]
    add_answer_to_question(answer="docker show images", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="docker image ls", is_correct=True, question_id=latest_id)
    add_answer_to_question(answer="docker inspect ls", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="docker display images", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="docker images", is_correct=True, question_id=latest_id)

    # 7
    add_question_to_quiz(question="You are running a web app container named webapp and you would like to access the web app outside of the docker host. The container is running on port 8080 and has its \
own internal ip address which is 127.0.0.10. The IP address of the host machine is 3.10.57.56. How should you access the web app outside of the host machine?", quiz_id=quiz_id)
    latest_id = get_latest_question_id_from_quiz(quiz_id=quiz_id)[0][0]
    add_answer_to_question(answer="Run the 'docker run webapp' command. Put 127.0.0.10:8080 into your browser.", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="Run the 'docker run -p 8080:8080 webapp' command. Put 127.0.0.10:8080 into your browser.", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="Run the 'docker run -p 8080:8080 webapp' command. Put 3.10.57.56:8080 into your browser.", is_correct=True, question_id=latest_id)
    add_answer_to_question(answer="Run the 'docker run webapp command' command. Put 3.10.57.56:8080 into your browser.", is_correct=False, question_id=latest_id)

    # 8
    add_question_to_quiz(question="John is developing a web application and he builds an image using the Dockerfile that he created. Recently, he has become very frustrated because every time he\
makes a code change he needs to rebuild the image to see the changes inside the container. How can he get around this problem?", quiz_id=quiz_id)
    latest_id = get_latest_question_id_from_quiz(quiz_id=quiz_id)[0][0]
    add_answer_to_question(answer="Inside the Dockerfile, add a 'RUN enable-automatic-update' command.", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="Create a docker-compose.yaml file and run the container using docker-compose up command instead.", is_correct=True, question_id=latest_id)
    add_answer_to_question(answer="The image always needs to be rebuild every time you make a code change.", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="He needs to run 'docker container update' command everytime he makes a code change.", is_correct=False, question_id=latest_id)
    
    # 9
    add_question_to_quiz(question="Tom is developing an applicaton locally. His application contains variables whose values are from the defined environment variables. For example, he uses MYSQL_ROOT_PASSWORD as one of his environment variables as the application is trying to access the MySQL database. His database password is abc124. He needs to pass the environment variable into the container but he wants to do this as securely as possible using docker. The name of this container is app1. Which of the following is the best option to do this?", quiz_id=quiz_id)
    latest_id = get_latest_question_id_from_quiz(quiz_id=quiz_id)[0][0]
    add_answer_to_question(answer="Use the ENV instruction in the Dockerfile to set the MYSQL_PASSWORD to abc124", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="Create a JSON file. Modify the application to pull the database password from this JSON file.", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="Run the 'docker run --secret MYSQL_ROOT_PASSWORD=abc123 app1' command", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="Run the 'docker run -e MYSQL_ROOT_PASSWORD=abc123 app1' command", is_correct=True, question_id=latest_id)
    
    # 10
    add_question_to_quiz(question="You have created a Dockerfile and now you want to build the image. The image must have the name 'my_new_image'. Which of the following is the valid docker command that you can use to achieve this?", quiz_id=quiz_id)
    latest_id = get_latest_question_id_from_quiz(quiz_id=quiz_id)[0][0]
    add_answer_to_question(answer="docker build -t my_new_image .", is_correct=True, question_id=latest_id)
    add_answer_to_question(answer="docker build --name my_new_image .", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="docker build Dockerfile my_new_image", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="docker build my_new_image .", is_correct=False, question_id=latest_id)

    # 11
    add_question_to_quiz(question="You want to run a new docker container from an image named 'saturn'. You would like to limit the amount of CPU and Memory that this new container uses. \
You would like the container to only use up to 10% of CPU and 140MB of memory. Which docker command will allow you to do this?", quiz_id=quiz_id)
    latest_id = get_latest_question_id_from_quiz(quiz_id=quiz_id)[0][0]
    add_answer_to_question(answer="docker run --cpus=0.1 --memory=140m saturn", is_correct=True, question_id=latest_id)
    add_answer_to_question(answer="docker run cpu=0.1 memory=140m saturn.", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="docker run saturn && docker set cpu = 0.1 saturn && docker set memory=140m saturn", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="docker exec --cpus=0.1 --memory=140m saturn", is_correct=False, question_id=latest_id)

    # 12
    add_question_to_quiz(question="You are developing an application and you would like to change some files inside the container. Which TWO statements regarding this action are true?", quiz_id=quiz_id)
    latest_id = get_latest_question_id_from_quiz(quiz_id=quiz_id)[0][0]
    add_answer_to_question(answer="You can directly write to the container layer to change the files inside the container.", is_correct=True, question_id=latest_id)
    add_answer_to_question(answer="You can directly write to the image layer to change the files inside the container.", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="You can rebuild the image to change the files inside the container.", is_correct=True, question_id=latest_id)
    add_answer_to_question(answer="You can use a 'docker container update' command to change the files inside the container", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="You can use a 'docker container write' command to change the files inside the container", is_correct=False, question_id=latest_id)

    # 13
    add_question_to_quiz(question="Which of the following is NOT a default docker network?", quiz_id=quiz_id)
    latest_id = get_latest_question_id_from_quiz(quiz_id=quiz_id)[0][0]
    add_answer_to_question(answer="Bridge", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="None", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="Host", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="Container", is_correct=True, question_id=latest_id)

    # 14
    add_question_to_quiz(question="Josh wants to create a new docker network which uses the bridge driver and IP address range 182.18.0.1/24 \
. He also wants to configure the Gateway to have an IP address of 182.18.0.1. The name of this network must be jsh_network. Which command will allow him to do this?", quiz_id=quiz_id)
    latest_id = get_latest_question_id_from_quiz(quiz_id=quiz_id)[0][0]
    add_answer_to_question(answer="docker create network --driver bridge --cidr 182.18.0.1/24 --gateway 182.18.0.1 jsh_network", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="docker create network --driver bridge --subnet 182.18.0.1/24 --gateway 182.18.0.1 jsh_network", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="docker network create --driver bridge --subnet 182.18.0.1/24 --gateway 182.18.0.1 jsh_network", is_correct=True, question_id=latest_id)
    add_answer_to_question(answer="docker network create --driver bridge --ip-range 182.18.0.1/24 --gateway 182.18.0.1 jsh_network", is_correct=False, question_id=latest_id)

    #15
    add_question_to_quiz(question="Which of the following is NOT a container orchestration tool?", quiz_id=quiz_id)
    latest_id = get_latest_question_id_from_quiz(quiz_id=quiz_id)[0][0]
    add_answer_to_question(answer="Docker swarm", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="Kubernetes", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="Docker orchestrator", is_correct=True, question_id=latest_id)
    add_answer_to_question(answer="MESOS", is_correct=False, question_id=latest_id)

    #16
    add_question_to_quiz(question="Alice wants to see what network the running container 'hubba_bubba' is attached to. What command can she use?", quiz_id=quiz_id)
    latest_id = get_latest_question_id_from_quiz(quiz_id=quiz_id)[0][0]
    add_answer_to_question(answer="docker network --name hubba_bubba ls", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="docker network inspect hubba_bubba", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="docker inspect network --target=hubba_bubba", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="docker inspect hubba_bubba", is_correct=True, question_id=latest_id)

    #17
    add_question_to_quiz(question="Gregory has created a new docker image named 'buggos' and his docker hub repository name is 'gregory12' \
. He wants to push this new image to this new repository that he has created on docker hub, but he gets a permission denied error. What can he do to fix this?", quiz_id=quiz_id)
    latest_id = get_latest_question_id_from_quiz(quiz_id=quiz_id)[0][0]
    add_answer_to_question(answer="He needs to generate an SSH key and copy and paste this new key on docker hub.", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="He needs to run the 'docker login' command using docker CLI and enter his username and password which corresponds to his docker hub account.", is_correct=True, question_id=latest_id)
    add_answer_to_question(answer="He needs to contact the docker hub team so that they can give him direct access to his newly created repository.", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="He needs to go to the docker hub website and go to his repository, then tick a box next to 'allow connections using docker CLI'.", is_correct=False, question_id=latest_id)

    #18
    add_question_to_quiz(question="Raymond has built a new image called 'sas-image'. He wants to run a container from this image and \
attach it to a new network that he created which is called 'sas-network'. He also wants to run this container in detached mode and the \
name of this new container must be 'ray-container'. Which docker command will allow him to do this? ", quiz_id=quiz_id)
    latest_id = get_latest_question_id_from_quiz(quiz_id=quiz_id)[0][0]
    add_answer_to_question(answer="docker run -d --name=ray-container --network=sas-network sas-image", is_correct=True, question_id=latest_id)
    add_answer_to_question(answer="docker run -it --name=ray-container --network=sas-network sas-image", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="docker exec -d --name=ray-container --network=sas-network sas-image", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="docker exec -dit --name ray-container --network sas-network sas-image", is_correct=False, question_id=latest_id)


create_docker_basics_quiz(user_id=1)

    
    