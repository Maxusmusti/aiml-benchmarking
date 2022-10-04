# Blender 3.3 Graphics Rendering

Baremetal Setup:
 - yum install -y epel-release
 - yum install -y phoronix-test-suite unzip xz
 - yum install @base-x
 - NO_FILE_HASH_CHECKS=1 phoronix-test-suite install blender
 - cd /var/lib/phoronix-test-suite/installed-tests/pts/blender-3.3.1/blender-3.3.0-linux-x64/
 - ./blender -b ../barbershop_interior_gpu.blend -o output.test -x 1 -F JPEG -f 1 -- --cycles-device CUDA
