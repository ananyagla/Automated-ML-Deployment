pipeline {
    agent any

    stages {

        stage('Clone Repo') {
            steps {
                git branch: 'main',
                url: 'https://github.com/ananyagla/Automated-ML-Deployment.git'
            }
        }

        stage('Trigger Render Deployment') {
            steps {
                sh 'curl -X POST https://api.render.com/deploy/YOUR_DEPLOY_HOOK'
            }
        }
    }
}