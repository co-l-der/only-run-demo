
**简要描述：**

统一多任务运行入口，提供工程化模板

1. 将所有任务按模块（如model, data, client）封装为Entry的子类（如ModelEntry, DataEntry, ClientEntry）

2. 将需要运行的Entry子类通过AppGenerator封装为核心对象(通常用app表示)

3. 在统一入口文件run.py中获取核心对象app, 该app提供多任务同步和异步调用方式（run, run_async）


**说明：**

1. 借鉴Flask项目结构和核心对象app概念

2. 借鉴Flask读取配置方式，见utils中config.py

