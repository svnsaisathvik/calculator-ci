pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "svnsaisathvik/imt2023001"
        TAG = "${env.BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM',
                    branches: [[name: '*/main']],
                    userRemoteConfigs: [[
                        url: 'https://github.com/svnsaisathvik/SE-Assignment',
                        credentialsId: 'github-creds'
                    ]]
                ])
            }
        }

        stage('Install') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                sh 'pytest -q'
            }
        }

        stage('Build Docker') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE}:${TAG} ."
            }
        }

        stage('Push Docker') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds',
                    usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh '''
                        echo "$PASS" | docker login -u "$USER" --password-stdin
                        docker push ${DOCKER_IMAGE}:${TAG}
                        docker logout
                    '''
                }
            }
        }
    }
}
