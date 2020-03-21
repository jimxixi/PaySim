--
-- 由SQLiteStudio v3.2.1 产生的文件 周日 3月 8 15:25:21 2020
--
-- 文本编码：UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- 表：account_table
DROP TABLE IF EXISTS account_table;

CREATE TABLE account_table (
    accountID      INTEGER PRIMARY KEY AUTOINCREMENT,
    openID         TEXT,
    accountState   TEXT,
    username       TEXT,
    password       TEXT,
    accountBalance INTEGER,
    checkTimestamp TEXT
);

INSERT INTO account_table (
                              accountID,
                              openID,
                              accountState,
                              username,
                              password,
                              accountBalance,
                              checkTimestamp
                          )
                          VALUES (
                              1,
                              'paysim',
                              'IDLE',
                              'paysim',
                              'admin',
                              100,
                              'notimestamp'
                          );

INSERT INTO account_table (
                              accountID,
                              openID,
                              accountState,
                              username,
                              password,
                              accountBalance,
                              checkTimestamp
                          )
                          VALUES (
                              2,
                              'testCustomer',
                              'IDLE',
                              'jimxixi',
                              'admin',
                              100,
                              'notimestamp'
                          );


-- 表：transaction_table
DROP TABLE IF EXISTS transaction_table;

CREATE TABLE transaction_table (
    transactionID    TEXT    PRIMARY KEY,
    transactionType  TEXT,
    tradeID          TEXT,
    transactionState TEXT    NOT NULL,
    source           TEXT    NOT NULL,
    target           TEXT    NOT NULL,
    sum              INTEGER NOT NULL,
    createTimestamp  TEXT,
    finishTimestamp  TEXT
);

INSERT INTO transaction_table (
                                  transactionID,
                                  transactionType,
                                  tradeID,
                                  transactionState,
                                  source,
                                  target,
                                  sum,
                                  createTimestamp,
                                  finishTimestamp
                              )
                              VALUES (
                                  'testTransaction',
                                  '主动转账',
                                  NULL,
                                  '未支付',
                                  'jimxixi',
                                  'paysim',
                                  1,
                                  NULL,
                                  NULL
                              );


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
