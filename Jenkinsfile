pipeline {
  agent any
  stages {
    stage('Code Quality') {
      steps {
        sh 'echo Checking code quality'
      }
    }

    stage('Unit Tests') {
      steps {
        sh 'echo Testing the application'
      }
    }

    stage('Build') {
      steps {
        sh 'echo Creating application package'
      }
    }

    stage('Delivery') {
      steps {
        sh 'echo Uploading the artifact to a repository'
      }
    }

    stage('Deploy') {
      steps {
        sh 'echo Deploying the application'
      }
    }

  }
}