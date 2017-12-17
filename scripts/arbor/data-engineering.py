import json

black_node = {'color': 'black'}
chocolate_node = {'color': 'chocolate'}
red_node = {'color': 'red'}
maroon_node = {'color': 'maroon'}

edge_data = {'color': '#b2b19d', 'width': 2}

params_height = 800
params_width = 400
params_padding_data = [160,160,160,160]

output = {}

content_nodes = 'nodes'
content_edges = 'edges'
content_params = 'params'
content_height = 'height'
content_width = 'width'
content_padding = 'padding'

content_data = 'data'
content_architectures = 'Architectures'
content_file_systems = 'File Systems'
content_data_stores = 'Data Stores'
content_lambda = 'Lambda'
content_kappa = 'Kappa'
content_summing_bird = 'SummingBird'
content_gfs = 'GFS'
content_hdfs = 'HDFS'
content_ceph_fs = 'Ceph File System'
content_alluxio = 'Alluxio, Inc'
content_kv_stores = 'KV Stores'
content_column_oriented = 'Column Oriented'
content_document_oriented = 'Document Oriented'
content_graph = 'Graph'
content_acid = 'ACID'
content_dynamo = "Dynamo"
content_cassandra = 'Cassandra'
content_voldemort = 'Voldemort'
content_bigtable = 'BigTable'
content_hbase = 'HBase'
content_hypertable = 'Hypertable'
content_couchdb = 'CouchDB'
content_mongodb = 'MongoDB'
content_neo4j = 'Neo4j'
content_titan = 'Titan'
content_megastore = 'Megastore'
content_spanner = 'Spanner'
content_mesa = 'MESA'
content_cockroachdb = 'CockroachDB'
content_resource_managers = 'Resource Managers'
content_yarn = 'Yarn'
content_mesos = 'Mesos'
content_coordination = 'Coordination'
content_paxos = 'Paxos'
content_chubby = 'Chubby'
content_zookeeper = 'Zookeeper'
content_raft = 'Raft'
content_messaging = 'Messaging'
content_kafka = 'Kafka'
content_flume = 'Flume'
content_sqoop = 'Sqoop'
content_computational_frameworks = 'Computational Frameworks'
content_spark = 'Spark'
content_flink = 'Flink'
content_map_reduce = 'Map Reduce'
content_storm = 'Storm'

nodes = {}
nodes[content_data] = black_node
nodes[content_architectures] = chocolate_node
nodes[content_file_systems] = chocolate_node
nodes[content_data_stores] = chocolate_node
nodes[content_lambda] = red_node
nodes[content_kappa] = red_node
nodes[content_summing_bird] = red_node
nodes[content_gfs] = red_node
nodes[content_hdfs] = red_node
nodes[content_ceph_fs] = red_node
nodes[content_alluxio] = red_node
nodes[content_kv_stores] = maroon_node
nodes[content_column_oriented] = maroon_node
nodes[content_document_oriented] = maroon_node
nodes[content_graph] = maroon_node
nodes[content_acid] = maroon_node
nodes[content_dynamo] = red_node
nodes[content_cassandra] = red_node
nodes[content_voldemort] = red_node
nodes[content_bigtable] = red_node
nodes[content_hbase] = red_node
nodes[content_hypertable] = red_node
nodes[content_couchdb] = red_node
nodes[content_mongodb] = red_node
nodes[content_neo4j] = red_node
nodes[content_titan] = red_node
nodes[content_megastore] = red_node
nodes[content_spanner] = red_node
nodes[content_mesa] = red_node
nodes[content_cockroachdb] = red_node
nodes[content_resource_managers] = chocolate_node
nodes[content_yarn] = red_node
nodes[content_mesos] = red_node
nodes[content_coordination] = chocolate_node
nodes[content_paxos] = red_node
nodes[content_chubby] = red_node
nodes[content_zookeeper] = red_node
nodes[content_raft] = red_node
nodes[content_messaging] = chocolate_node
nodes[content_kafka] = red_node
nodes[content_flume] = red_node
nodes[content_sqoop] = red_node
nodes[content_computational_frameworks] = chocolate_node
nodes[content_spark] = red_node
nodes[content_flink] = red_node
nodes[content_map_reduce] = red_node
nodes[content_storm] = red_node

output[content_nodes] = nodes

edges = {}

edge_data_node = {}
edge_data_node[content_architectures] = edge_data
edge_data_node[content_file_systems] = edge_data
edge_data_node[content_data_stores] = edge_data
edge_data_node[content_resource_managers] = edge_data
edge_data_node[content_coordination] = edge_data
edge_data_node[content_messaging] = edge_data
edge_data_node[content_computational_frameworks] = edge_data
edges[content_data] = edge_data_node

edge_architecture_node = {}
edge_architecture_node[content_lambda] = edge_data
edge_architecture_node[content_kappa] = edge_data
edge_architecture_node[content_summing_bird] = edge_data
edges[content_architectures] = edge_architecture_node

edge_file_systems_node = {}
edge_file_systems_node[content_gfs] = edge_data
edge_file_systems_node[content_hdfs] = edge_data
edge_file_systems_node[content_ceph_fs] = edge_data
edge_file_systems_node[content_alluxio] = edge_data
edges[content_file_systems] = edge_file_systems_node

edge_data_stores_node = {}
edge_data_stores_node[content_kv_stores] = edge_data
edge_data_stores_node[content_column_oriented] = edge_data
edge_data_stores_node[content_document_oriented] = edge_data
edge_data_stores_node[content_graph] = edge_data
edge_data_stores_node[content_acid] = edge_data
edges[content_data_stores] = edge_data_stores_node

edge_kv_stores_node = {}
edge_kv_stores_node[content_dynamo] = edge_data
edge_kv_stores_node[content_cassandra] = edge_data
edge_kv_stores_node[content_voldemort] = edge_data
edges[content_kv_stores] = edge_kv_stores_node

edge_column_oriented_node = {}
edge_column_oriented_node[content_bigtable] = edge_data
edge_column_oriented_node[content_hbase] = edge_data
edge_column_oriented_node[content_hypertable] = edge_data
edges[content_column_oriented] = edge_column_oriented_node

edge_document_oriented_node = {}
edge_document_oriented_node[content_couchdb] = edge_data
edge_document_oriented_node[content_mongodb] = edge_data
edges[content_document_oriented] = edge_document_oriented_node

edge_graph_node = {}
edge_graph_node[content_neo4j] = edge_data
edge_graph_node[content_titan] = edge_data
edges[content_graph] = edge_graph_node

edge_acid_node = {}
edge_acid_node[content_megastore] = edge_data
edge_acid_node[content_spanner] = edge_data
edge_acid_node[content_mesa] = edge_data
edge_acid_node[content_cockroachdb] = edge_data
edges[content_acid] = edge_acid_node

edges_resource_managers_node = {}
edges_resource_managers_node[content_yarn] = edge_data
edges_resource_managers_node[content_mesos] = edge_data
edges[content_resource_managers] = edges_resource_managers_node

edges_coordination_node = {}
edges_coordination_node[content_paxos] = edge_data
edges_coordination_node[content_chubby] = edge_data
edges_coordination_node[content_zookeeper] = edge_data
edges_coordination_node[content_raft] = edge_data
edges[content_coordination] = edges_coordination_node

edges_messaging_node = {}
edges_messaging_node[content_kafka] = edge_data
edges_messaging_node[content_flume] = edge_data
edges_messaging_node[content_sqoop] = edge_data
edges[content_messaging] = edges_messaging_node

edges_computational_frameworks_node = {}
edges_computational_frameworks_node[content_spark] = edge_data
edges_computational_frameworks_node[content_flink] = edge_data
edges_computational_frameworks_node[content_map_reduce] = edge_data
edges_computational_frameworks_node[content_storm] = edge_data
edges[content_computational_frameworks] = edges_computational_frameworks_node

output[content_edges] = edges

params = {}
params[content_height] = params_height
params[content_width] = params_width
params[content_padding] = params_padding_data

output[content_params] = params

json_string = json.dumps(output, sort_keys=True, indent=4)
arbor_string = '```arbor\n' + json_string + '\n```'
print arbor_string
