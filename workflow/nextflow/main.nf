
nextflow.enable.dsl=2

process EchoStart {
    output:
    path 'results/echo.txt'

    script:
    '''
    mkdir -p results
    cat << 'EOF' > results/echo.txt
    Precision Oncology Platform - Nextflow stub
    EOF
    '''
}

workflow {
    EchoStart()
}
