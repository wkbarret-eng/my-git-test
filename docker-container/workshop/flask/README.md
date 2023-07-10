# Docker Image exmaple

## Build
sudo docker build . -t docker-flask

## Run
sudo docker run -ti -p 5001:5001 9317a9f6ac4e 

## VOLUME

#### inner container
```bash=
$ sudo docker container ls
CONTAINER ID   IMAGE          COMMAND                  CREATED          STATUS          PORTS                                       NAMES
4fc68209e000   25b6c289ca8a   "/bin/sh -c 'python3…"   44 seconds ago   Up 43 seconds   0.0.0.0:5001->5001/tcp, :::5001->5001/tcp   goofy_galois
bcba90d3d482   f985963d1861   "/bin/sh -c 'python3…"   12 minutes ago   Up 12 minutes                                               nifty_knuth
yillkid@devops:~$ sudo docker exec -ti 4fc68209e000 bash
root@4fc68209e000:/app# cat logs/log.txt 
Daemon start!root@4fc68209e000:/app#
```

#### outter container
```bash=
$ sudo docker inspect 4fc68209e000

[
    {
        "Id": "4fc68209e00078ab846b6ab485cc4730e118c9d283094968b0975112822cd1fb",
        "Created": "2023-07-10T17:00:36.559179593Z",
        "Path": "/bin/sh",
        "Args": [
            "-c",
            "python3 server.py"
        ],
        "State": {
            "Status": "running",
            "Running": true,
            "Paused": false,
            "Restarting": false,
            "OOMKilled": false,
            "Dead": false,
            "Pid": 20173,
            "ExitCode": 0,
            "Error": "",
            "StartedAt": "2023-07-10T17:00:37.346631313Z",
            "FinishedAt": "0001-01-01T00:00:00Z"
        },
        "Image": "sha256:25b6c289ca8a138c68aa7e3344862eb3c82c2e1dd2d153ace7f9a0e551de33a0",
        "ResolvConfPath": "/var/lib/docker/containers/4fc68209e00078ab846b6ab485cc4730e118c9d283094968b0975112822cd1fb/resolv.conf",
        "HostnamePath": "/var/lib/docker/containers/4fc68209e00078ab846b6ab485cc4730e118c9d283094968b0975112822cd1fb/hostname",
        "HostsPath": "/var/lib/docker/containers/4fc68209e00078ab846b6ab485cc4730e118c9d283094968b0975112822cd1fb/hosts",
        "LogPath": "/var/lib/docker/containers/4fc68209e00078ab846b6ab485cc4730e118c9d283094968b0975112822cd1fb/4fc68209e00078ab846b6ab485cc4730e118c9d283094968b0975112822cd1fb-json.log",
        "Name": "/goofy_galois",
        "RestartCount": 0,
        "Driver": "overlay2",
        "Platform": "linux",
        "MountLabel": "",
        "ProcessLabel": "",
        "AppArmorProfile": "docker-default",
        "ExecIDs": [
            "004f4daf430c57552ba193109377282123557562bad37daa2412e2039fbf65a6"
        ],
        "HostConfig": {
            "Binds": null,
            "ContainerIDFile": "",
            "LogConfig": {
                "Type": "json-file",
                "Config": {}
            },
            "NetworkMode": "default",
            "PortBindings": {
                "5001/tcp": [
                    {
                        "HostIp": "",
                        "HostPort": "5001"
                    }
                ]
            },
            "RestartPolicy": {
                "Name": "no",
                "MaximumRetryCount": 0
            },
            "AutoRemove": false,
            "VolumeDriver": "",
            "VolumesFrom": null,
            "CapAdd": null,
            "CapDrop": null,
            "CgroupnsMode": "private",
            "Dns": [],
            "DnsOptions": [],
            "DnsSearch": [],
            "ExtraHosts": null,
            "GroupAdd": null,
            "IpcMode": "private",
            "Cgroup": "",
            "Links": null,
            "OomScoreAdj": 0,
            "PidMode": "",
            "Privileged": false,
            "PublishAllPorts": false,
            "ReadonlyRootfs": false,
            "SecurityOpt": null,
            "UTSMode": "",
            "UsernsMode": "",
            "ShmSize": 67108864,
            "Runtime": "runc",
            "ConsoleSize": [
                0,
                0
            ],
            "Isolation": "",
            "CpuShares": 0,
            "Memory": 0,
            "NanoCpus": 0,
            "CgroupParent": "",
            "BlkioWeight": 0,
            "BlkioWeightDevice": [],
            "BlkioDeviceReadBps": null,
            "BlkioDeviceWriteBps": null,
            "BlkioDeviceReadIOps": null,
            "BlkioDeviceWriteIOps": null,
            "CpuPeriod": 0,
            "CpuQuota": 0,
            "CpuRealtimePeriod": 0,
            "CpuRealtimeRuntime": 0,
            "CpusetCpus": "",
            "CpusetMems": "",
            "Devices": [],
            "DeviceCgroupRules": null,
            "DeviceRequests": null,
            "KernelMemory": 0,
            "KernelMemoryTCP": 0,
            "MemoryReservation": 0,
            "MemorySwap": 0,
            "MemorySwappiness": null,
            "OomKillDisable": null,
            "PidsLimit": null,
            "Ulimits": null,
            "CpuCount": 0,
            "CpuPercent": 0,
            "IOMaximumIOps": 0,
            "IOMaximumBandwidth": 0,
            "MaskedPaths": [
                "/proc/asound",
                "/proc/acpi",
                "/proc/kcore",
                "/proc/keys",
                "/proc/latency_stats",
                "/proc/timer_list",
                "/proc/timer_stats",
                "/proc/sched_debug",
                "/proc/scsi",
                "/sys/firmware"
            ],
            "ReadonlyPaths": [
                "/proc/bus",
                "/proc/fs",
                "/proc/irq",
                "/proc/sys",
                "/proc/sysrq-trigger"
            ]
        },
        "GraphDriver": {
            "Data": {
                "LowerDir": "/var/lib/docker/overlay2/3dd54e098421037410c9f549a48c6903abeda86f3f7eec375e5ad251f967b8ac-init/diff:/var/lib/docker/overlay2/b143118538fc4713bded74f1746e08989c30eb9400eba2e7ddfa4c12812e74aa/diff:/var/lib/docker/overlay2/ce0adc3630edcdde99a3a0a5dc94a657d371853b9af36c1ea0b80dbe7f24eecb/diff:/var/lib/docker/overlay2/fb5d1906f888950c8788b9dfe5cb233630c694b84e5c8159037b1082e5312935/diff:/var/lib/docker/overlay2/085db20e794cbb995140ec06c15930c4f2f360b5de0f16bb5fa343eea575b95e/diff:/var/lib/docker/overlay2/2a65b08d60362614403633b6c0e44a229387b7cb77fddd07b7e4e1b6647827af/diff:/var/lib/docker/overlay2/64662cd30969a60a496ff7871b67b5b5d77eff98caf439614b82241bfe507763/diff:/var/lib/docker/overlay2/b988a217d5be70cdb5109d6202401b533e7e562cc9f427d1c8020c04bad223e5/diff:/var/lib/docker/overlay2/7cee40be7763bac5a54a9c225cad6a60049fbfbcc25cccb1c0959114ffdf9bd0/diff:/var/lib/docker/overlay2/e909c4a7401373835fa05beb0eccae5e35fad646f8ce9360e6c42cebd58ca18b/diff:/var/lib/docker/overlay2/1ea3eccf8358640ee27c1d3c3984abc32c554051b3c55574f29eed474befa8e5/diff:/var/lib/docker/overlay2/34f9b375c0afe8ca8a43d56c2639488d7e43352e294581c3577a068a19de88dc/diff:/var/lib/docker/overlay2/68dfc09cc02cb3455f9964c1f1326537d24a6734e31084ec1ef512ce78f48a14/diff",
                "MergedDir": "/var/lib/docker/overlay2/3dd54e098421037410c9f549a48c6903abeda86f3f7eec375e5ad251f967b8ac/merged",
                "UpperDir": "/var/lib/docker/overlay2/3dd54e098421037410c9f549a48c6903abeda86f3f7eec375e5ad251f967b8ac/diff",
                "WorkDir": "/var/lib/docker/overlay2/3dd54e098421037410c9f549a48c6903abeda86f3f7eec375e5ad251f967b8ac/work"
            },
            "Name": "overlay2"
        },
        "Mounts": [
            {
                "Type": "volume",
                "Name": "739dd07d8960c59c3b025ebc98676ef2d141dee6522001b1dad8602c9bd4eac7",
                "Source": "/var/lib/docker/volumes/739dd07d8960c59c3b025ebc98676ef2d141dee6522001b1dad8602c9bd4eac7/_data",
                "Destination": "/app/logs",
                "Driver": "local",
                "Mode": "",
                "RW": true,
                "Propagation": ""
            }
        ],
        "Config": {
            "Hostname": "4fc68209e000",
            "Domainname": "",
            "User": "",
            "AttachStdin": true,
            "AttachStdout": true,
            "AttachStderr": true,
            "ExposedPorts": {
                "5001/tcp": {}
            },
            "Tty": true,
            "OpenStdin": true,
            "StdinOnce": true,
            "Env": [
                "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
                "LANG=C.UTF-8",
                "GPG_KEY=0D96DF4D4110E5C43FBFB17F2D347EA6AA65421D",
                "PYTHON_VERSION=3.6.9",
                "PYTHON_PIP_VERSION=19.3.1",
                "PYTHON_GET_PIP_URL=https://github.com/pypa/get-pip/raw/ffe826207a010164265d9cc807978e3604d18ca0/get-pip.py",
                "PYTHON_GET_PIP_SHA256=b86f36cc4345ae87bfd4f10ef6b2dbfa7a872fbff70608a1e43944d283fd0eee"
            ],
            "Cmd": [
                "/bin/sh",
                "-c",
                "python3 server.py"
            ],
            "Image": "25b6c289ca8a",
            "Volumes": {
                "/app/logs": {}
            },
            "WorkingDir": "/app",
            "Entrypoint": null,
            "OnBuild": null,
            "Labels": {
                "version": "= 1.0 Copyright = 2022 owner = yillkid"
            }
        },
        "NetworkSettings": {
            "Bridge": "",
            "SandboxID": "4fc85c5d99861548e37b726d25d781f9e11d170a16cf0eae34d642f74b908146",
            "HairpinMode": false,
            "LinkLocalIPv6Address": "",
            "LinkLocalIPv6PrefixLen": 0,
            "Ports": {
                "5001/tcp": [
                    {
                        "HostIp": "0.0.0.0",
                        "HostPort": "5001"
                    },
                    {
                        "HostIp": "::",
                        "HostPort": "5001"
                    }
                ]
            },
            "SandboxKey": "/var/run/docker/netns/4fc85c5d9986",
            "SecondaryIPAddresses": null,
            "SecondaryIPv6Addresses": null,
            "EndpointID": "420c48f079b819d2ef17ae7533b43ec8c88f86d8ceb9662af386cc4728b15a13",
            "Gateway": "172.17.0.1",
            "GlobalIPv6Address": "",
            "GlobalIPv6PrefixLen": 0,
            "IPAddress": "172.17.0.3",
            "IPPrefixLen": 16,
            "IPv6Gateway": "",
            "MacAddress": "02:42:ac:11:00:03",
            "Networks": {
                "bridge": {
                    "IPAMConfig": null,
                    "Links": null,
                    "Aliases": null,
                    "NetworkID": "45abb298c343fd86182b78ce30a53632c7bb46c2be5b291f0e53c82223d98909",
                    "EndpointID": "420c48f079b819d2ef17ae7533b43ec8c88f86d8ceb9662af386cc4728b15a13",
                    "Gateway": "172.17.0.1",
                    "IPAddress": "172.17.0.3",
                    "IPPrefixLen": 16,
                    "IPv6Gateway": "",
                    "GlobalIPv6Address": "",
                    "GlobalIPv6PrefixLen": 0,
                    "MacAddress": "02:42:ac:11:00:03",
                    "DriverOpts": null
                }
            }
        }
    }
]
```

```bash=
$ sudo cat /var/lib/docker/volumes/739dd07d8960c59c3b025ebc98676ef2d141dee6522001b1dad8602c9bd4eac7/_data/log.txt
Daemon start!
```
