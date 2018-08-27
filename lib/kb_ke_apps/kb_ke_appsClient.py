# -*- coding: utf-8 -*-
############################################################
#
# Autogenerated by the KBase type compiler -
# any changes made here will be overwritten
#
############################################################

from __future__ import print_function
# the following is a hack to get the baseclient to import whether we're in a
# package or not. This makes pep8 unhappy hence the annotations.
try:
    # baseclient and this client are in a package
    from .baseclient import BaseClient as _BaseClient  # @UnusedImport
except:
    # no they aren't
    from baseclient import BaseClient as _BaseClient  # @Reimport


class kb_ke_apps(object):

    def __init__(
            self, url=None, timeout=30 * 60, user_id=None,
            password=None, token=None, ignore_authrc=False,
            trust_all_ssl_certificates=False,
            auth_svc='https://kbase.us/services/authorization/Sessions/Login'):
        if url is None:
            raise ValueError('A url is required')
        self._service_ver = None
        self._client = _BaseClient(
            url, timeout=timeout, user_id=user_id, password=password,
            token=token, ignore_authrc=ignore_authrc,
            trust_all_ssl_certificates=trust_all_ssl_certificates,
            auth_svc=auth_svc)

    def run_hierarchical_cluster(self, params, context=None):
        """
        run_hierarchical_cluster: generates hierarchical clusters for Matrix data object
        :param params: instance of type "HierClusterParams" (Input of the
           run_hierarchical_cluster function matrix_ref: Matrix object
           reference workspace_name: the name of the workspace
           feature_set_suffix: suffix append to FeatureSet object name
           dist_threshold: the threshold to apply when forming flat clusters
           Optional arguments: dist_metric: The distance metric to use.
           Default set to 'euclidean'. The distance function can be
           ["braycurtis", "canberra", "chebyshev", "cityblock",
           "correlation", "cosine", "dice", "euclidean", "hamming",
           "jaccard", "kulsinski", "matching", "rogerstanimoto",
           "russellrao", "sokalmichener", "sokalsneath", "sqeuclidean",
           "yule"] Details refer to:
           https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.
           distance.pdist.html linkage_method: The linkage algorithm to use.
           Default set to 'ward'. The method can be ["single", "complete",
           "average", "weighted", "centroid", "median", "ward"] Details refer
           to:
           https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.
           hierarchy.linkage.html fcluster_criterion: The criterion to use in
           forming flat clusters. Default set to 'distance'. The criterion
           can be ["inconsistent", "distance", "maxclust"] Details refer to:
           https://docs.scipy.org/doc/scipy/reference/generated/scipy.cluster.
           hierarchy.fcluster.html) -> structure: parameter "matrix_ref" of
           type "obj_ref" (An X/Y/Z style reference), parameter
           "workspace_name" of String, parameter "feature_set_suffix" of
           String, parameter "dist_threshold" of Double, parameter
           "dist_metric" of String, parameter "linkage_method" of String,
           parameter "fcluster_criterion" of String
        :returns: instance of type "HierClusterOutput" (Ouput of the
           run_hierarchical_cluster function feature_set_set_refs: a list of
           result FeatureSetSet object references report_name: report name
           generated by KBaseReport report_ref: report reference generated by
           KBaseReport) -> structure: parameter "feature_set_set_refs" of
           list of type "obj_ref" (An X/Y/Z style reference), parameter
           "report_name" of String, parameter "report_ref" of String
        """
        return self._client.call_method(
            'kb_ke_apps.run_hierarchical_cluster',
            [params], self._service_ver, context)

    def run_kmeans_cluster(self, params, context=None):
        """
        run_kmeans_cluster: generates Kmeans clusters for Matrix data object
        :param params: instance of type "KmeansClusterParams" (Input of the
           run_kmeans_cluster function matrix_ref: Matrix object reference
           workspace_name: the name of the workspace cluster_set_suffix:
           suffix append to KBaseExperiments.ClusterSet object name k_num:
           number of clusters to form Optional arguments: dist_metric: The
           distance metric to use. Default set to 'euclidean'. The distance
           function can be ["braycurtis", "canberra", "chebyshev",
           "cityblock", "correlation", "cosine", "dice", "euclidean",
           "hamming", "jaccard", "kulsinski", "matching", "rogerstanimoto",
           "russellrao", "sokalmichener", "sokalsneath", "sqeuclidean",
           "yule"] Details refer to:
           https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.
           distance.pdist.html) -> structure: parameter "matrix_ref" of type
           "obj_ref" (An X/Y/Z style reference), parameter "workspace_name"
           of String, parameter "cluster_set_suffix" of String, parameter
           "k_num" of Long, parameter "dist_metric" of String
        :returns: instance of type "KmeansClusterOutput" (Ouput of the
           run_kmeans_cluster function cluster_set_refs:
           KBaseExperiments.ClusterSet object references report_name: report
           name generated by KBaseReport report_ref: report reference
           generated by KBaseReport) -> structure: parameter
           "cluster_set_refs" of list of type "obj_ref" (An X/Y/Z style
           reference), parameter "report_name" of String, parameter
           "report_ref" of String
        """
        return self._client.call_method(
            'kb_ke_apps.run_kmeans_cluster',
            [params], self._service_ver, context)

    def run_pca(self, params, context=None):
        """
        run_pca: generates PCA matrix for KBaseExperiments.ClusterSet data object
        :param params: instance of type "PCAParams" (Input of the run_pca
           function cluster_set_ref: KBaseExperiments.ClusterSet object
           references workspace_name: the name of the workspace
           pca_matrix_suffix: suffix append to PCA
           (KBaseFeatureValues.FloatMatrix2D) object name) -> structure:
           parameter "cluster_set_ref" of type "obj_ref" (An X/Y/Z style
           reference), parameter "workspace_name" of String, parameter
           "pca_matrix_suffix" of String
        :returns: instance of type "PCAOutput" (Ouput of the run_pca function
           pca_ref: PCA object reference (as KBaseFeatureValues.FloatMatrix2D
           data type) report_name: report name generated by KBaseReport
           report_ref: report reference generated by KBaseReport) ->
           structure: parameter "pca_ref" of type "obj_ref" (An X/Y/Z style
           reference), parameter "report_name" of String, parameter
           "report_ref" of String
        """
        return self._client.call_method(
            'kb_ke_apps.run_pca',
            [params], self._service_ver, context)

    def status(self, context=None):
        return self._client.call_method('kb_ke_apps.status',
                                        [], self._service_ver, context)
