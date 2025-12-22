pipeline {
  agent any

  stages {
    stage('clone') {
      steps {
        git 'https://github.com/anazif-yn/practice.git'
        echo 'Repository cloned!'
      }
    }

    stage('List Files') {
      steps {
        sh 'ls -la'
      }
    }

    stage('Build') {
      steps {
        echo 'Building Project...'
      }
    }
  }
}
