import sqlite3
import time
import uuid
import json

DB = sqlite3.connect(r"C:\Users\admin\Desktop\jdf\PaySim\PaySim.db")
Cursor = DB.cursor()

# util
def makeTimeStamp() -> str:
    return str(int(1000 * time.time()))

def makeUUID() -> str:
    return str(uuid.uuid4())

# 业务逻辑的实现，一律返回字典对象
def CreateAccount(username: str, password: str, initBalance: int) -> dict:
    # 创建账户（用户名，密码，初始金额）
    Cursor.execute(f'insert into account_table (username, password, accountBalance, checkTimestamp) values ("{username}", "{password}", {initBalance}, "{makeTimeStamp()}")')
    data = {"result": "创建成功", "openID": "无"}
    DB.commit()
    return data
def BindWechat(username: str, openID: str) -> dict:
    # 绑定微信（用户名，微信open ID）
    Cursor.execute(f'update account_table set openID="{openID}"" where username={username}')
    DB.commit()
    return {"result": "绑定完成"}
def FreezeAccount(username: str) -> dict:
    # 冻结账户（用户名）
    Cursor.execute(f'update account_table set accountState="冻结" where username="{username}"')
    data = {"result": "冻结成功"}
    DB.commit()
    return data
def UpdateAccountRecharge(username: str, sum: int) -> dict:
    # 充值（用户名，金额）
    oldSum = Cursor.execute(f"select accountBalance from account_table where username='{username}'").fetchone()[0]
    Cursor.execute(f"update account_table set accountBalance={oldSum+sum} where username='{username}'")
    data = {"result": "充值成功"}
    DB.commit()
    return data
def UpdateAccountCashout(username: str, sum: int) -> dict:
    # 提现（用户名，金额）
    Cursor.execute("")
    data = {"result": "提现失败"}
    DB.commit()
    return data
def CheckAccount(username: str) -> dict:
    # 查询账户（用户名）
    Cursor.execute(f'select openID, accountState, accountBalance, checkTimestamp from account_table where username="{username}"')
    result = Cursor.fetchone()
    data = {"openID": result[0], "accountState": result[1], "accountBalance": result[2], "checkTimestamp": result[3]}
    return data
def AccountTransfer(source: str, target: str, sum: int) -> dict:
    # 主动转账（转账用户名，收款用户名，金额）
    ID = makeUUID()
    Cursor.execute(f'insert into transaction_table (transactionID, transactionType, transactionState, source, target, sum, createTimestamp) values ("{ID}", "主动转账", "未完成", "{source}", "{target}", {sum}, "{makeTimeStamp()}")')
    data = {"result": "转账失败", "transactionID": ID}
    DB.commit()
    return data
def StartTrade(target: str, source: str, tradeID: str, sum: int, timeLimit: int) -> dict:
    # 发起交易（商家用户名，散客用户名，商家内部订单号，金额，支付时限）
    ID = makeUUID()
    Cursor.execute(f'insert into transaction_table (transactionID, transactionType, transactionState, source, target, sum, createTimestamp) values ("{ID}", "交易", "待支付", "{source}", "{target}", "{sum}", "{makeTimeStamp()}")')
    data = {"result": "交易创建失败", "transactionID": ID}
    DB.commit()
    return data
def PayoffTrade(tradeID: str, username: str, password: str) -> dict:
    # 支付交易（商家内部订单号，用户名，密码）
    Cursor.execute(f'update transaction_table transactionState="已支付" where tradeID="{tradeID}"')
    data = {"result": "支付成功"}
    DB.commit()
    return data
def QueryTrade(tradeID: str) -> dict:
    # 查询交易（商家内部订单号）
    Cursor.execute(f'select transactionID, tradeID, tradeState, source, target from transaction_table where tradeID={tradeID}')
    result = Cursor.fetchone()
    data = {"transactionID": result[0], "tradeID": result[1], "tradeState": result[2], "source": result[3], "target": result[4]}
    return data


if __name__ == "__main__":
    idd = makeUUID()
    print(idd)
    print(str(idd))
    # print("测试PayLib.py: ")
    # print(CreateAccount("测试用户1", "123456", 100))
    # print(UpdateAccountRecharge("测试用户1", 100))
    # print(CheckAccount("测试用户1"))


