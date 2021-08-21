__author__ = "raviusit@gmail.com"

import re
from lib import logging as logger
from lib.get_crds import K8sCRDs
from lib.get_pods import K8sPods
from lib.get_svc import K8sService
from lib.get_deploy import K8sDeploy
from lib.get_ds import K8sDaemonSet
from lib.get_sts import K8sStatefulSet
from lib.get_ns import K8sNameSpace
from lib.get_ingress import K8sIngress
from lib.get_jobs import K8sJobs
from lib.get_rbac import K8sClusterRole, K8sNameSpaceRole, K8sNameSpaceRoleBinding


class Cluster:
    def get_cluster_name(self):
        from lib.get_cm import K8sConfigMap

        cm = K8sConfigMap.get_cm("kube-system")
        for item in cm.items:
            if "kubeadm-config" in item.metadata.name:
                if "clusterName" in item.data["ClusterConfiguration"]:
                    cluster_name = re.search(
                        r"clusterName: ([\s\S] )controlPlaneEndpoint",
                        item.data["ClusterConfiguration"],
                    ).group(1)
                    print(cluster_name)
                    return cluster_name
            else:
                pass


def main():
    instance = Cluster()
    _logger = logger.get_logger("Cluster")
    K8sCRDs.get_crds()
    K8sNameSpace.get_ns()
    K8sClusterRole.list_cluster_role()
    K8sJobs.get_jobs("kube-system")
    K8sPods.get_pods("kube-system")
    K8sService.get_svc("kube-system")
    K8sStatefulSet.get_sts("kube-system")
    K8sIngress.get_ingress("kube-system")
    K8sDeploy.get_deployments("kube-system")
    K8sDaemonSet.get_damemonsets("kube-system")
    K8sNameSpaceRole.list_namespaced_role("kube-system")
    K8sNameSpaceRoleBinding.list_namespaced_role_binding("kube-system")


if __name__ == "__main__":
    main()
