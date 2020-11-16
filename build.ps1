#
# build.ps1
#
# Build and deploy a new version of maxar_catalog by doing the following:
#
# 1.  Update the build number maxarcat/version.txt
# 2.  Build a new wheel by running python setup.py bdist_wheel
# 3.  Run pip install on the new wheel
#

$ErrorActionPreference = 'Stop'
Set-StrictMode -Version Latest

function UpdatePackageVersion($VersionFile)
{
    Write-Host "Reading $VersionFile"
    $Version = Get-Content -Raw $VersionFile
    Write-Host "Current Version:  $Version"

    $Parts = $Version -split '\.'
    $Parts[-1] = [String]([Int]$Parts[-1] + 1)
    $NewVersion = [String]::Join('.', $Parts)
    Write-Host "New Version:      $NewVersion"

    Write-Host "Writing new version to $VersionFile"
    [System.IO.File]::WriteAllText($VersionFile, $NewVersion)

    return $NewVersion
}

# Get the repo's toplevel directory, assuming this build.ps1 script is at the top level
$ThisScript = $MyInvocation.MyCommand.Source
$RootDir = Split-Path -Parent $ThisScript

$PackageVersionFile = Join-Path $RootDir 'maxarcat\version.txt'
$NewVersion = UpdatePackageVersion $PackageVersionFile

python setup.py bdist_wheel
if ($LASTEXITCODE -ne 0) {
    throw "Python setup error"
}

dir dist

$WheelName = "maxarcat-$NewVersion-py3-none-any.whl"
pip install "dist/$WheelName"
