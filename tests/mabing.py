from paste.deploy import loadapp
import os
here = "."
result = loadapp('config:sample_configs/basic_app.ini', relative_to=here)
print result, result.__class__
import inspect
print inspect.getsource(result)  # 这里直接返回basic_app这个函数的源码