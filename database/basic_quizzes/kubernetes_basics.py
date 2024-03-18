
from database.database import add_answer_to_question, add_question_to_quiz, add_quiz_to_user, get_latest_question_id_from_quiz, get_latest_quiz_id_from_user


def create_kubernetes_basics_quiz(user_id: int):
    add_quiz_to_user(name="Kubernetes Basics", ongoing=False, pass_rate=70, user_id=user_id)
    quiz_id = get_latest_quiz_id_from_user(user_id=user_id)[0][0]

    # 1
    add_question_to_quiz(question="Which of the following kubernetes components is responsible for distributing load across multiple nodes?", quiz_id=quiz_id)
    latest_id = get_latest_question_id_from_quiz(quiz_id=quiz_id)[0][0]
    add_answer_to_question(answer="Scheduler", is_correct=True, question_id=latest_id)
    add_answer_to_question(answer="Controller", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="Kubelet", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="Etcd", is_correct=False, question_id=latest_id)

    # 2
    add_question_to_quiz(question="Which of the following kubectl commands shows information about the cluster?", quiz_id=quiz_id)
    latest_id = get_latest_question_id_from_quiz(quiz_id=quiz_id)[0][0]
    add_answer_to_question(answer="kubectl cluster ls", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="kubectl cluster-info", is_correct=True, question_id=latest_id)
    add_answer_to_question(answer="kubectl inspect cluster", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="kubectl get nodes", is_correct=False, question_id=latest_id)

    # 3
    add_question_to_quiz(question="Which of the following CLIs work with containerd? (SELECT TWO)", quiz_id=quiz_id)
    latest_id = get_latest_question_id_from_quiz(quiz_id=quiz_id)[0][0]
    add_answer_to_question(answer="ctr", is_correct=True, question_id=latest_id)
    add_answer_to_question(answer="crictl", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="nerdctl", is_correct=True, question_id=latest_id)
    add_answer_to_question(answer="ctrdctl", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="kubectl", is_correct=False, question_id=latest_id)

    # 4
    add_question_to_quiz(question="A kubernetes cluster currently has three nodes and you would like to see what operating system each node is running on. \
What command can he use?", quiz_id=quiz_id)
    latest_id = get_latest_question_id_from_quiz(quiz_id=quiz_id)[0][0]
    add_answer_to_question(answer="kubectl inspect nodes", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="kubectl node ls", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="kubectl get nodes", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="kubectl get nodes -o wide", is_correct=True, question_id=latest_id)

    # 5
    add_question_to_quiz(question="You would like to see some details about a new pod that was created in the kubernetes cluster such as the IP address of the pod, \
the namespace and the containers running inside it. The name of this pod is 'bob'. What command can he use?", quiz_id=quiz_id)
    latest_id = get_latest_question_id_from_quiz(quiz_id=quiz_id)[0][0]
    add_answer_to_question(answer="kubectl get pods --details --pod=bob", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="kubectl get pods -o wide --pod=bob", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="kubectl describe pod bob", is_correct=True, question_id=latest_id)
    add_answer_to_question(answer="kubectl inspect pod bob", is_correct=False, question_id=latest_id)

    # 6
    add_question_to_quiz(question="You want to create a pod in a kubernetes cluster and for this you need to create a YAML file. Which of the properties below are required for this YAML file? (SELECT THREE)", quiz_id=quiz_id)
    latest_id = get_latest_question_id_from_quiz(quiz_id=quiz_id)[0][0]
    add_answer_to_question(answer="config", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="metadata", is_correct=True, question_id=latest_id)
    add_answer_to_question(answer="setting", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="description", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="apiVersion", is_correct=True, question_id=latest_id)
    add_answer_to_question(answer="spec", is_correct=True, question_id=latest_id)

    # 7
    add_question_to_quiz(question="Adam has created a new YAML file which is used to create a new replica set. The name of this replica set is 'adam_replica_set. \
He soon realizes that he does not have enough pods to handle the load from multiple users, so he needs to create more pods to achieve this. \
He currently has 3 pods in the cluster, but he needs to scale up to 5 pods. Which of the following are possible ways of scaling the number of pods? (SELECT TWO)", quiz_id=quiz_id)
    latest_id = get_latest_question_id_from_quiz(quiz_id=quiz_id)[0][0]
    add_answer_to_question(answer="Delete the current replica set and edit the replica set YAML file. Change the 'replicas' value from 3 to 5.", is_correct=True, question_id=latest_id)
    add_answer_to_question(answer="Edit the replica set YAML file. Add more pods under the template property of the YAML file.", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="Edit the pod YAML file. Change the 'replicas' value from 3 to 5. ", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="Use the 'kubectl edit replicaset adam_replica_set --replicas=5' command. ", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="Use the 'kubectl scale replicaset adam_replica_set --replicas=5' command", is_correct=True, question_id=latest_id)

    # 8
    add_question_to_quiz(question="You want to upgrade your web application to a newer version so you decide to perform a rolling update. However, after some time \
you realize that something is not quite right and you would like to rollback to the previous deployment. Which command will allow you to do this?", quiz_id=quiz_id)
    latest_id = get_latest_question_id_from_quiz(quiz_id=quiz_id)[0][0]
    add_answer_to_question(answer="kubectl undo deployment/webapp-deployment", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="kubectl rollout undo deployment/webapp-deployment", is_correct=True, question_id=latest_id)
    add_answer_to_question(answer="kubectl rollback deployment/webapp-deployment", is_correct=False, question_id=latest_id)
    add_answer_to_question(answer="kubectl reverse rollout deployment/webapp-deployment", is_correct=False, question_id=latest_id)


create_kubernetes_basics_quiz(user_id=1)