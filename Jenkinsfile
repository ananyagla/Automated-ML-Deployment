pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'main', url: 'https://github.com/ananyagla/Automated-ML-Deployment.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Train Models') {
            steps {
                sh 'python train_all.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t automated-ml .'
            }
        }

        stage('Deploy to Render') {
            steps {
                sh '''
                curl -X POST 'https://api.render.com/deploy/srv-d6heqh7kijhs73ffbni0?key=Z7kSZZyqm5c'
                '''
            }
        }
    }
}