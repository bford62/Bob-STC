node() {

    def repoURL = 'https://github.com/bford62/Bob-STC.git'

    stage("Prepare Workspace") {
        echo "*** Prepare Workspace ***"
		cleanWs()
		env.WORKSPACE_LOCAL = sh(returnStdout: true, script: 'pwd').trim()
		env.BUILD_TIME = "${BUILD_TIMESTAMP}"
        echo "Workspace set to:" + env.WORKSPACE_LOCAL
        echo "Build time:" + env.BUILD_TIME
    }
    stage('Checkout Self') {
		echo "*** Checking Code Out ***"
        git branch: 'main', credentialsId: '', url: repoURL
    }
    stage('Cucumber Tests') {
		echo "*** Execute Test Cases ***"
        sh """
        cd ${env.WORKSPACE_LOCAL}
        ls -CFla
        """
    }
    stage('Expose report') {
		echo "*** Expose Reports ***"
		echo "*** Archive Artifacts ***"
        // archiveArtifacts "**/cucumber.json"
		echo "*** cucumber cucumber.json ***"
        /* cucumber '**/cucumber.json'
		junit skipPublishingChecks: true, allowEmptyResults: true, keepLongStdio: true, testResults: 'storetarget-bdd/reporting/junit_xml/*.xml' */
    }
	stage('Import results to Xray') {
		echo "*** Import Results to XRAY ***"

/*		def description = "[TEST_BUILD_URL|${env.BUILD_URL}]"
		def labels = '["regression","automated_regression"]'
		def environment = "DEV"
		def testExecutionFieldId = 10552
		def testEnvironmentFieldName = "customfield_10372"
		def projectKey = "Xray-Test"
		def projectId = 10606
		def xrayConnectorId = "${xrayConnectorId}"
		def info = '''{
				"fields": {
					"project": {
					"id": "''' + projectId + '''"
				},
				"labels":''' + labels + ''',
				"description":"''' + description + '''",
				"summary": "Testing Jenkins - Automated Regression Execution @ ''' + env.BUILD_TIME + ' ' + environment + ''' " ,
				"issuetype": {
				"id": "''' + testExecutionFieldId + '''"
				}
				}
				}'''

			echo info

			step([$class: 'XrayImportBuilder', endpointName: '/cucumber/multipart', importFilePath: 'storetarget-bdd/reporting/cucumber.json', importInfo: info, inputInfoSwitcher: 'fileContent', serverInstance: xrayConnectorId]) */
		}
}