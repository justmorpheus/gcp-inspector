<p align="center">
   <img alt="GCP Inspector" src="https://i.ibb.co/7G3ptg9/gcp-inspector-final.png" width="400"/>
</p>

**Tool to check publicly accessible GCP bucket.**

## Blog
- https://justm0rph3u5.medium.com/gcp-inspector-auditing-publicly-exposed-gcp-bucket-ac6cad55618c

## What it does
 - Checks whether the GCP bucket from the list is publicly accessible or not.
 - Provides colored description in the cli.
After creating a new project and enabling billing for it, open Cloud Shell and ensure that it points to the project you just created.

## Prerequisites
### GCP account with project.
 - **Create a GCP account with project enabled**
   - Install [gsutil tool](https://cloud.google.com/storage/docs/gsutil) from the documentation or use pip.
   - Run "gsutil config" to configure shell. Else use “gcloud config set project [PROJECT_ID]” to set the project to any other project (external account for attacker's perspective) for checking publicly accessible bucket.
   - Run "gsutil ls" to check the command is successful. This will list all the google buckets for project.
   - Install python3 and pip for installting dependencies.
   - GCP Bucket listing with or without gs:// from the file via path as an argument.

## Installation
###Python3 virtual environment is required.
```
python3 -m pip install gsutil
gsutil config OR “gcloud config set project [PROJECT_ID]”
git clone https://github.com/justmorpheus/GCP-Inspector
cd GCP-Inspector
mkdir gcp_inspect
virtualenv -v gcp_inspect
source gcp_inspect/bin/activate
python3 -m pip install -r requirements.txt
python3 gcp_inspector.py -r sample_file.txt
```

## Usage
`python3 gcp_inspector.py -r [Name of the file with GCP bucket list]`

![image](https://user-images.githubusercontent.com/86191568/127789592-852f30e8-0b5e-45fe-9847-258f19236db3.png)

## Reference
- https://docs.google.com/presentation/d/1R7mSTbra24z5uj9N6botjkaXuneSvVV6AK5siKnFrcw/htmlpresent
- https://github.com/clario-tech/s3-inspector
- https://github.com/NicholasSpringer/thunder-ctf

[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](http://buymeacoffee.com/justmorpheus)

