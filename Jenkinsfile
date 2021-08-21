// Author :- raviusit@gmail.com
/* groovylint-disable CompileStatic, NestedBlockDepth */

pipeline {
    options {
        disableConcurrentBuilds()
        ansiColor('xterm')
    }
    agent {
        kubernetes {
            defaultContainer 'jnlp'
            yaml"""
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: jnlp
    image: jnlp-alpine:4.3.4
    args: ['\$(JENKINS_SECRET)', '\$(JENKINS_NAME)']
  - name: docker
    image: docker:19.03
    command:
    - cat
    tty: true
    volumeMounts:
    - name: dockersock
      mountPath: /var/run/docker.sock
  volumes:
  - name: dockersock
    hostPath:
      path: /var/run/docker.sock
"""
        }
    }
    environment {
        PROTOCOL = 'https://'
        IMAGE_TAG =  'v1'
        CONTAINER_DOCKER = 'docker'
        IMAGE_NAME = 'k8s-python-framework'
        //TARGET_CREDENTIAL = ''
        //ARTIFACTORY = ''
    }
    stages {
        stage('build-k8s-python-framework-image') {
            steps {
                script {
                    container(CONTAINER_DOCKER) {
                        docker.withRegistry(PROTOCOL + ARTIFACTORY, TARGET_CREDENTIAL) {
                            sh 'docker build -t $ARTIFACTORY/$IMAGE_NAME:$IMAGE_TAG .'
                        }
                    }
                }
            }
        }
        stage('push-k8s-python-framework-image') {
            steps {
                script {
                    container(CONTAINER_DOCKER) {
                        docker.withRegistry(PROTOCOL + ARTIFACTORY, TARGET_CREDENTIAL) {
                            sh 'docker push $ARTIFACTORY/$IMAGE_NAME:$IMAGE_TAG'
                        }
                    }
                }
            }
        }
    }
}
