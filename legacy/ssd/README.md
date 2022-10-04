# MLPerf Training 0.7 Nvidia SSD
For baremetal setup:
 - git clone https://github.com/mlcommons/training_results_v0.7.git
 - cd training_results_v0.7/NVIDIA/benchmarks/ssd/implementations/pytorch/
 - ./download_dataset.sh
 - mkdir /path/to/coco/results

To Run:
 - podman run --security-opt=no-new-privileges --cap-drop=ALL --security-opt label=type:nvidia_container_t --ipc=host -v /path/to/coco/:/storage/:z -it quay.io/openshift-psap/ci-artifacts:mlperf-ssd-training-benchmark /bin/bash
 - Run `./ssd-entrypoint.sh 2>&1 | tee /storage/results/results.txt` using provided file
 - Run `analyze.py` on the results file to get avg samples/sec

For OpenShift:
 - oc create secret generic s3-secret --from-file=cococred.csv=/path/to/cococred.csv
 - oc apply -f ssd-pvc.yml
 - oc apply -f coco_entrypoint.yml
 - oc apply -f ssd_entrypoint.yml
 - oc create -f setup-pod.yml
 - oc create -f ssd-pod.yml 
