#
# generate-client.ps1
#
# Run swagger codegen on the Maxar Catalog OpenAPI specification,
# creating the maxarcat_client Python package.  This only has to be
# done when the Maxar Catalog OpenAPI specification changes.
#
# Run swagger codegen using the Docker image swaggerapi/swagger-codegen-cli-v3.
# See https://hub.docker.com/r/swaggerapi/swagger-codegen-cli-v3
#
# For the parameter OpenApiSpecUrl specify the URL of the OpenAPI specification
# that we document for public users.  Generally use the OpenAPI spec published
# to the Maxar Catalog documentation website:
#
#     .\generate-client.ps1 https://doc.content.maxar.com/maxar-content-catalog.json
#
# When testing you might want to generate a client using an OpenAPI file on your
# workstation.  In this case pass the location of the OpenAPI file as it appears
# mounted in the Docker container, for example something like
# "/maxarcat/open_api.yaml"
#

param([Parameter(Mandatory=$True)]$OpenApiSpecUrl)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'

$DockerImage = 'swaggerapi/swagger-codegen-cli-v3'
$ClientDirName = 'maxarcat_client'
$ConfigFilename = "maxarcat_client_config.json"
$VolumeMount = '/maxarcat'

$ThisScript = $MyInvocation.MyCommand.Path
$RepoDir = Split-Path -Parent $ThisScript

# Create the output directory for the generated code, first deleting existing dir if necessary
$ClientDir = Join-Path $RepoDir $ClientDirName
Write-Host "Generating swagger client to $ClientDir"
if (Test-Path $ClientDir)
{
    Write-Host "Deleting existing client dir: $ClientDir"
    Remove-Item -Rec -Force $ClientDir
}
Write-Host "Creating client dir: $ClientDir"
mkdir $ClientDir

Write-Host "Running docker image $DockerImage"
Write-Host "Mounting $RepoDir to $VolumeMount"

# Run swagger codegen.
# Note how we remap "datetime" to "search_datetime".  The issue is that
# the STAC search API has a query parameter "datetime" which is easily
# confused with Python's datetime.
docker run --rm -v "${RepoDir}:$VolumeMount" $DockerImage generate `
    --input-spec $OpenApiSpecUrl `
    --lang python `
    --output "$VolumeMount/$ClientDirName" `
    --reserved-words-mappings datetime=search_datetime `
    --config "$VolumeMount/$ConfigFilename"
