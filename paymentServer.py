import platform
if platform.system() == "Windows":
    import asyncio
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

import tornado.ioloop
import tornado.web
import PayLib
import json

MethodDict = {
    "发起交易": PayLib.StartTrade,
    "支付交易": PayLib.PayoffTrade,
    "查询交易": PayLib.QueryTrade,
}

class PaySim(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.set_header("Access-Control-Allow-Origin", "*")
    def get(self):
        print(self)
        self.write("hello汉字测试")
    def post(self):
        argDict = json.loads(self.request.body)
        print(argDict)
        method = argDict['method']
        if method == "发起交易":
            res = PayLib.StartTrade(argDict['target'], argDict['source'], argDict['tradeID'], argDict['sum'], argDict['timeLimit'])
        elif method == "支付交易":
            res = PayLib.PayoffTrade(argDict['tradeID'], argDict['username'], argDict['password'])
        elif method == "查询交易":
            res = PayLib.QueryTrade(argDict['tradeID'])
        else:
            res = {"result": "执行失败，请检查参数是否符合接口文档"}
        print("执行结果：", res)
        self.write(json.dumps(res))

app = tornado.web.Application(
    [
        (r"/PaySim", PaySim),
    ]
)
app.listen(20056)
tornado.ioloop.IOLoop.current().start()


