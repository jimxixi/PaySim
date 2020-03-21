# 账户管理数据库

## 资金账户表

- int accountID
- String openID
- String accountState
- String username
- String password
- Integer accountBalance
- String checkTimestamp

## 转帐表

- int transactionID   uuid
- String transactionType "主动转账", "交易"
- String tradeID "商家系统内部订单号"
- String transactionState
- String sourceID
- String targetID
- Integer sum
- String createTimestamp
- String finishTimestamp

## accountState账户状态枚举

IDLE - 空闲
FROZEN - 冻结
BUSY - 阻塞

## tradeState交易状态枚举

SUCCESS—支付成功

REFUND—转入退款

NOTPAY—未支付

CLOSED—已关闭

REVOKED—已撤销（刷卡支付）

USERPAYING--用户支付中

PAYERROR--支付失败(其他原因，如银行返回失败)

