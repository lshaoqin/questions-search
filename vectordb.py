from milvus import default_server
from pymilvus import connections, utility

# (OPTIONAL) Set if you want store all related data to specific location
# Default location:
#   %APPDATA%/milvus-io/milvus-server on windows
#   ~/.milvus-io/milvus-server on linux
# default_server.set_base_dir('milvus_data')

# (OPTIONAL) if you want cleanup previous data
# default_server.cleanup()

with default_server:
  default_server.set_base_dir('milvus_data')

with default_server:
  # Milvus Lite has already started, use default_server here.
  connections.connect(host='127.0.0.1', port=default_server.listen_port)