# NvidiaDL BERT Fine-Tuning

For baremetal setup:
 - git clone https://github.com/Maxusmusti/DeepLearningExamples.git
 - cd DeepLearningExamples/
 - git checkout -b vgpu origin/vgpu
 - cd TensorFlow2/LanguageModeling/BERT/
 - bash scripts/data_download.sh squad

To run:
 - bash scripts/docker/launch.sh
 - bash scripts/run_squad.sh 1 12 5e-6 fp16 true large 1.1 2

For OpenShift:
 - Make sure there is a persistent volume available
 - oc apply -f bert-pvc.yml
 - oc apply -f bert_setup_entrypoint.yml
 - oc create -f bertsetup.yml
 - oc create -f squad-download.yml
 - oc create -f bert-pod.yml 
