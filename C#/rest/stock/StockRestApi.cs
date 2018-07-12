using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace com.okcoin.rest.stock
{
    /// <summary>
    /// 现货行情，交易 REST API
    /// </summary>
    class StockRestApi : IStockRestApi
    {
        /// <summary>
        /// OKCoin申请的secretKey
        /// </summary>
        private String secret_key;
        /// <summary>
        /// OKCoin申请的apiKey
        /// </summary>
        private String api_key;
        /// <summary>
        /// 请求URL 国际站https://www.okcoin.com ; 国内站https://www.okcoin.cn
        /// </summary>
        private String url_prex;
        public String getSecret_key()
        {
            return secret_key;
        }

        public void setSecret_key(String secret_key)
        {
            this.secret_key = secret_key;
        }

        public String getApi_key()
        {
            return api_key;
        }

        public void setApi_key(String api_key)
        {
            this.api_key = api_key;
        }

        public String getUrl_prex()
        {
            return url_prex;
        }

        public void setUrl_prex(String url_prex)
        {
            this.url_prex = url_prex;
        }
        public StockRestApi(String url_prex, String api_key, String secret_key)
        {
            this.api_key = api_key;
            this.secret_key = secret_key;
            this.url_prex = url_prex;
        }

        public StockRestApi(String url_prex)
        {
            this.url_prex = url_prex;
        }

        /// <summary>
        /// 现货行情URL
        /// </summary>
        private const String TICKER_URL = "/api/v1/ticker.do";

        /// <summary>
        /// 现货市场深度URL
        /// </summary>
        private const String DEPTH_URL = "/api/v1/depth.do";

        /// <summary>
        /// 现货历史交易信息URL
        /// </summary>
        private const String TRADES_URL = "/api/v1/trades.do";
        /// <summary>
        /// 现货的K线数据
        /// </summary>
        private const String KLINE_URL = "/api/v1/kline.do";
        /// <summary>
        /// 现货获取用户信息URL
        /// </summary>
        private const String USERINFO_URL = "/api/v1/userinfo.do";

        /// <summary>
        /// 现货 下单交易URL
        /// </summary>
        private const String TRADE_URL = "/api/v1/trade.do";

        /// <summary>
        /// 现货 批量下单URL
        /// </summary>
        private const String BATCH_TRADE_URL = "/api/v1/batch_trade.do";

        /// <summary>
        /// 现货 撤销订单URL
        /// </summary>
        private const String CANCEL_ORDER_URL = "/api/v1/cancel_order.do";

        /// <summary>
        /// 现货 获取用户订单URL
        /// </summary>
        private const String ORDER_INFO_URL = "/api/v1/order_info.do";

        /// <summary>
        /// 现货 批量获取用户订单URL
        /// </summary>
        private const String ORDERS_INFO_URL = "/api/v1/orders_info.do";

        /// <summary>
        /// 现货 获取历史订单信息，只返回最近七天的信息URL
        /// </summary>
        private const String ORDER_HISTORY_URL = "/api/v1/order_history.do";
        /// <summary>
        /// 提币BTC/LTCD的URL
        /// </summary>
        private const String WITHDRAW_URL = "/api/v1/withdraw.do";
        /// <summary>
        /// 取消提币BTC/LTC
        /// </summary>
        private const String CANCEL_WITHDRAW_RUL = "/api/v1/cancel_withdraw.do";
        /// <summary>
        /// 查询手续费
        /// </summary>
        private const String ORDER_FEE_URL = "/api/v1/order_fee.do";
        /// <summary>
        ///  获取放款深度前10
        /// </summary>
        private const String LEND_DEPTH_URL = "/api/v1/lend_depth.do";
        private const String BORROWS_INFO_URL = "/api/v1/borrows_info.do";
        /// <summary>
        ///  申请借款
        /// </summary>
        private const String BORROW_MONEY_URL = "/api/v1/borrow_money.do";
        /// <summary>
        /// 取消借款申请
        /// </summary>
        private const String CANCEL_BORROW_URL = "/api/v1/cancel_borrow.do";
        /// <summary>
        /// 获取借款订单记录
        /// </summary>
        private const String BORROW_ORDER_INFO = "/api/v1/borrow_order_info.do";
        /// <summary>
        /// 用户还全款
        /// </summary>
        private const String REPAYMENT_URL = "/api/v1/repayment.do";
        /// <summary>
        /// 未还款列表
        /// </summary>
        private const String UNREPAYMENTS_INFO_URL = "/api/v1/unrepayments_info.do";
        /// <summary>
        /// 获取用户提现/充值记录
        /// </summary>
        private const String ACCOUNT_RECORDS_URL = "/api/v1/account_records.do";
        /// <summary>
        ///  获取历史交易信息
        /// </summary>
        private const String TRADE_HISTORY_URL = "/api/v1/trade_history.do";
        /// <summary>
        /// 行情
        /// </summary>
        /// <param name="symbol">btc_usd:比特币    ltc_usd :莱特币</param>
        /// <returns></returns>
        public String ticker(String symbol)
        {
            String result = "";
            try
            {
                HttpUtilManager httpUtil = HttpUtilManager.getInstance();
                String param = "";
                if (!StringUtil.isEmpty(symbol))
                {
                    if (!param.Equals(""))
                    {
                        param += "&";
                    }
                    param += "symbol=" + symbol;
                }
                result = httpUtil.requestHttpGet(url_prex, TICKER_URL, param);
            }
            catch (Exception e)
            {
                throw e;
            }
            return result;
        }

        /// <summary>
        /// 现货市场深度
        /// </summary>
        /// <param name="symbol">btc_usd:比特币    ltc_usd :莱特币</param>
        /// <param name="size">size:1-200</param>
        /// <returns></returns>
        public String depth(String symbol, String size)
        {
            String result = "";
            try
            {
                HttpUtilManager httpUtil = HttpUtilManager.getInstance();
                String param = "";
                if (!StringUtil.isEmpty(symbol))
                {
                    if (!param.Equals(""))
                    {
                        param += "&";
                    }
                    param += "symbol=" + symbol;
                }
                if (!StringUtil.isEmpty(size))
                {
                    if (!param.Equals(""))
                    {
                        param += "&";
                    }
                    param += "size=" + size;
                }
                result = httpUtil.requestHttpGet(url_prex, DEPTH_URL, param);
            }
            catch (Exception e)
            {
                throw e;
            }
            return result;
        }

        /// <summary>
        /// 现货历史交易信息
        /// </summary>
        /// <param name="symbol">btc_usd:比特币    ltc_usd :莱特币</param>
        /// <param name="since">不加since参数时，返回最近的60笔交易</param>
        /// <returns></returns>
        public String trades(String symbol, String since)
        {
            String result = "";
            try
            {
                HttpUtilManager httpUtil = HttpUtilManager.getInstance();
                String param = "";
                if (!StringUtil.isEmpty(symbol))
                {
                    if (!param.Equals(""))
                    {
                        param += "&";
                    }
                    param += "symbol=" + symbol;
                }
                if (!StringUtil.isEmpty(since))
                {
                    if (!param.Equals(""))
                    {
                        param += "&";
                    }
                    param += "since=" + since;
                }
                result = httpUtil.requestHttpGet(url_prex, TRADES_URL, param);
            }
            catch (Exception e)
            {
                throw e;
            }
            return result;
        }
        /// <summary>
        /// 现货的K线数据
        /// </summary>
        /// <param name="symbol">btc_usd：比特币， ltc_usd：莱特币 </param>
        /// <param name="type">
        /// 1min : 1分钟 
        /// 3min : 3分钟 
        /// 5min : 5分钟 
        /// 15min : 15分钟 
        /// 30min : 30分钟
        /// 1day : 1日
        /// 3day : 3日
        ///1week : 1周
        ///1hour : 1小时
        ///2hour : 2小时
        ///4hour : 4小时
        ///6hour : 6小时
        ///12hour : 12小时</param>
        /// <param name="size">指定获取数据的条数</param>
        /// <param name="since">时间戳（eg：1417536000000）。 返回该时间戳以后的数据 </param>
        /// <returns></returns>
        public String kline(String symbol, String type, String size, String since)
        {
            String result = "";
            try
            {
                HttpUtilManager httpUtil = HttpUtilManager.getInstance();
                String param = "";
                if (!StringUtil.isEmpty(symbol))
                {
                    if (!param.Equals(""))
                    {
                        param += "&";
                    }
                    param += "symbol=" + symbol;
                }
                if (!StringUtil.isEmpty(type))
                {
                    if (!param.Equals(""))
                    {
                        param += "&";
                    }
                    param += "type=" + type;
                }
                if (!StringUtil.isEmpty(size))
                {
                    if (!param.Equals(""))
                    {
                        param += "&";
                    }
                    param += "size=" + size;
                }
                if (!StringUtil.isEmpty(since))
                {
                    if (!param.Equals(""))
                    {
                        param += "&";
                    }
                    param += "since=" + since;
                }
                result = httpUtil.requestHttpGet(url_prex, KLINE_URL, param);
            }
            catch (Exception e)
            {
                throw e;
            }
            return result;
        }
        /// <summary>
        /// 获取用户信息
        /// </summary>
        /// <returns></returns>
        public String userinfo()
        {
            String result = "";
            try
            {
                // 构造参数签名
                Dictionary<String, String> paras = new Dictionary<String, String>();
                paras.Add("api_key", api_key);
                String sign = MD5Util.buildMysignV1(paras, this.secret_key);
                paras.Add("sign", sign);

                // 发送post请求
                HttpUtilManager httpUtil = HttpUtilManager.getInstance();
                result = httpUtil.requestHttpPost(url_prex, USERINFO_URL,
                       paras);
            }
            catch (Exception e)
            {
                throw e;
            }
            return result;
        }

        /// <summary>
        /// 下单交易
        /// </summary>
        /// <param name="symbol">btc_usd: 比特币 ltc_usd: 莱特币</param>
        /// <param name="type">买卖类型： 限价单（buy/sell） 市价单（buy_market/sell_market）</param>
        /// <param name="price">下单价格 [限价买单(必填)： 大于等于0，小于等于1000000 |  市价买单(必填)： BTC :最少买入0.01个BTC 的金额(金额>0.01*卖一价) / LTC :最少买入0.1个LTC 的金额(金额>0.1*卖一价)]</param>
        /// <param name="amount"> 交易数量 [限价卖单（必填）：BTC 数量大于等于0.01 / LTC 数量大于等于0.1 | 市价卖单（必填）： BTC :最少卖出数量大于等于0.01 / LTC :最少卖出数量大于等于0.1]</param>
        /// <returns></returns>
        public String trade(String symbol, String type,
                String price, String amount)
        {
            String result = "";
            try
            {
                // 构造参数签名
                Dictionary<String, String> paras = new Dictionary<String, String>();
                paras.Add("api_key", api_key);
                if (!StringUtil.isEmpty(symbol))
                {
                    paras.Add("symbol", symbol);
                }
                if (!StringUtil.isEmpty(type))
                {
                    paras.Add("type", type);
                }
                if (!StringUtil.isEmpty(price))
                {
                    paras.Add("price", price);
                }
                if (!StringUtil.isEmpty(amount))
                {
                    paras.Add("amount", amount);
                }
                String sign = MD5Util.buildMysignV1(paras, this.secret_key);
                paras.Add("sign", sign);

                // 发送post请求
                HttpUtilManager httpUtil = HttpUtilManager.getInstance();
                result = httpUtil.requestHttpPost(url_prex, TRADE_URL,
                       paras);
            }
            catch (Exception e)
            {
                throw e;
            }

            return result;
        }
        /// <summary>
        /// 批量下单
        /// </summary>
        /// <param name="symbol">btc_usd: 比特币 ltc_usd: 莱特币</param>
        /// <param name="type">买卖类型： 限价单（buy/sell） 市价单（buy_market/sell_market）</param>
        /// <param name="orders_data">JSON类型的字符串 例：[{price:3,amount:5},{price:3,amount:3}]   最大下单量为5，price和amount参数参考trade接口中的说明</param>
        /// <returns></returns>
        public String batch_trade(String symbol, String type,
                String orders_data)
        {
            String result = "";
            try
            { // 构造参数签名
                Dictionary<String, String> paras = new Dictionary<String, String>();
                paras.Add("api_key", api_key);
                if (!StringUtil.isEmpty(symbol))
                {
                    paras.Add("symbol", symbol);
                }
                if (!StringUtil.isEmpty(type))
                {
                    paras.Add("type", type);
                }
                if (!StringUtil.isEmpty(orders_data))
                {
                    paras.Add("orders_data", orders_data);
                }
                String sign = MD5Util.buildMysignV1(paras, this.secret_key);
                paras.Add("sign", sign);

                // 发送post请求
                HttpUtilManager httpUtil = HttpUtilManager.getInstance();
                result = httpUtil.requestHttpPost(url_prex, BATCH_TRADE_URL,
                       paras);
            }
            catch (Exception e)
            {
                throw e;
            }
            return result;
        }

        /// <summary>
        /// 撤销订单
        /// </summary>
        /// <param name="symbol">btc_usd: 比特币 ltc_usd: 莱特币</param>
        /// <param name="order_id">订单ID(多个订单ID中间以","分隔,一次最多允许撤消3个订单)</param>
        /// <returns></returns>
        public String cancel_order(String symbol, String order_id)
        {
            String result = "";
            try
            {// 构造参数签名
                Dictionary<String, String> paras = new Dictionary<String, String>();
                paras.Add("api_key", api_key);
                if (!StringUtil.isEmpty(symbol))
                {
                    paras.Add("symbol", symbol);
                }
                if (!StringUtil.isEmpty(order_id))
                {
                    paras.Add("order_id", order_id);
                }

                String sign = MD5Util.buildMysignV1(paras, this.secret_key);
                paras.Add("sign", sign);

                // 发送post请求
                HttpUtilManager httpUtil = HttpUtilManager.getInstance();
                result = httpUtil.requestHttpPost(url_prex, CANCEL_ORDER_URL,
                       paras);
            }
            catch (Exception e)
            {
                throw e;
            }

            return result;
        }

        /// <summary>
        /// 获取用户的订单信息
        /// </summary>
        /// <param name="symbol">btc_usd: 比特币 ltc_usd: 莱特币</param>
        /// <param name="order_id">订单ID(-1查询全部订单，否则查询相应单号的订单)</param>
        /// <returns></returns>
        public String order_info(String symbol, String order_id)
        {
            String result = "";
            try
            { // 构造参数签名
                Dictionary<String, String> paras = new Dictionary<String, String>();
                paras.Add("api_key", api_key);
                if (!StringUtil.isEmpty(symbol))
                {
                    paras.Add("symbol", symbol);
                }
                if (!StringUtil.isEmpty(order_id))
                {
                    paras.Add("order_id", order_id);
                }

                String sign = MD5Util.buildMysignV1(paras, this.secret_key);
                paras.Add("sign", sign);

                // 发送post请求
                HttpUtilManager httpUtil = HttpUtilManager.getInstance();
                result = httpUtil.requestHttpPost(url_prex, ORDER_INFO_URL,
                        paras);
            }
            catch (Exception e)
            {
                throw e;
            }
            return result;
        }

        /// <summary>
        /// 批量获取用户订单
        /// </summary>
        /// <param name="type">查询类型 0:未成交，未成交 1:完全成交，已撤销</param>
        /// <param name="symbol">btc_usd: 比特币 ltc_usd: 莱特币</param>
        /// <param name="order_id">订单ID(多个订单ID中间以","分隔,一次最多允许查询50个订单)</param>
        /// <returns></returns>
        public String orders_info(String type, String symbol,
                String order_id)
        {
            String result = "";
            try
            {
                // 构造参数签名
                Dictionary<String, String> paras = new Dictionary<String, String>();
                paras.Add("api_key", api_key);
                if (!StringUtil.isEmpty(type))
                {
                    paras.Add("type", type);
                }
                if (!StringUtil.isEmpty(symbol))
                {
                    paras.Add("symbol", symbol);
                }
                if (!StringUtil.isEmpty(order_id))
                {
                    paras.Add("order_id", order_id);
                }

                String sign = MD5Util.buildMysignV1(paras, this.secret_key);
                paras.Add("sign", sign);

                // 发送post请求
                HttpUtilManager httpUtil = HttpUtilManager.getInstance();
                result = httpUtil.requestHttpPost(url_prex, ORDERS_INFO_URL,
                        paras);
            }
            catch (Exception e)
            {
                throw e;
            }

            return result;
        }

        /// <summary>
        /// 获取历史订单信息，只返回最近七天的信息
        /// </summary>
        /// <param name="symbol">btc_usd: 比特币 ltc_usd: 莱特币</param>
        /// <param name="status">委托状态: 0：未成交 1：已完成(最近七天的数据)</param>
        /// <param name="current_page">当前页数</param>
        /// <param name="page_length">每页数据条数，最多不超过200</param>
        /// <returns></returns>
        public String order_history(String symbol, String status,
                String current_page, String page_length)
        {
            String result = "";
            try
            {
                // 构造参数签名
                Dictionary<String, String> paras = new Dictionary<String, String>();
                paras.Add("api_key", api_key);
                if (!StringUtil.isEmpty(symbol))
                {
                    paras.Add("symbol", symbol);
                }
                if (!StringUtil.isEmpty(status))
                {
                    paras.Add("status", status);
                }
                if (!StringUtil.isEmpty(current_page))
                {
                    paras.Add("current_page", current_page);
                }
                if (!StringUtil.isEmpty(page_length))
                {
                    paras.Add("page_length", page_length);
                }

                String sign = MD5Util.buildMysignV1(paras, this.secret_key);
                paras.Add("sign", sign);

                // 发送post请求
                HttpUtilManager httpUtil = HttpUtilManager.getInstance();
                result = httpUtil.requestHttpPost(url_prex, ORDER_HISTORY_URL,
                        paras);
            }
            catch (Exception e)
            {
                throw e;
            }

            return result;
        }
        /// <summary>
        /// 提币BTC/LTC
        /// </summary>
        /// <param name="symbol">btc_usd: 比特币 ltc_usd: 莱特币 </param>
        /// <param name="chargefee">网络手续费 BTC默认范围 [0.0001，0.01] LTC默认范围 [0.001，0.2],手续费越高，网络确认越快，OKCoin内部提币设置0 </param>
        /// <param name="trade_pwd">交易密码 </param>
        /// <param name="withdraw_address">提币认证地址 </param>
        /// <param name="withdraw_amount">提币数量 BTC>=0.01 LTC>=0.1 </param>
        /// <returns></returns>
        public String withdraw(String symbol, String chargefee, String trade_pwd, String withdraw_address, String withdraw_amount)
        {
            String result = "";
            try
            {
                Dictionary<String, String> paras = new Dictionary<String, String>();
                paras.Add("api_key", api_key);
                if (!StringUtil.isEmpty(symbol))
                {
                    paras.Add("symbol", symbol);
                }
                if (!StringUtil.isEmpty(chargefee))
                {
                    paras.Add("chargefee", chargefee);
                }
                if (!StringUtil.isEmpty(trade_pwd))
                {
                    paras.Add("trade_pwd", trade_pwd);
                }
                if (!StringUtil.isEmpty(withdraw_address))
                {
                    paras.Add("withdraw_address", withdraw_address);
                }
                if (!StringUtil.isEmpty(withdraw_amount))
                {
                    paras.Add("withdraw_amount", withdraw_amount);
                }
                String sign = MD5Util.buildMysignV1(paras, this.secret_key);
                paras.Add("sign", sign);

                // 发送post请求
                HttpUtilManager httpUtil = HttpUtilManager.getInstance();
                result = httpUtil.requestHttpPost(url_prex, WITHDRAW_URL,
                        paras);
            }
            catch (Exception e)
            {
                throw e;
            }
            return result;
        }
        /// <summary>
        /// 取消提币BTC/LTC
        /// </summary>
        /// <param name="symbol">btc_usd: 比特币 ltc_usd: 莱特币 </param>
        /// <param name="withdraw_id">提币申请Id </param>
        /// <returns></returns>
        public String cancel_withdraw(String symbol, String withdraw_id)
        {
            String result = "";
            try
            {
                HttpUtilManager httpUtil = HttpUtilManager.getInstance();
                Dictionary<String, String> paras = new Dictionary<String, String>();
                paras.Add("api_key", api_key);
                if (!StringUtil.isEmpty(symbol))
                {
                    paras.Add("symbol", symbol);
                }
                if (!StringUtil.isEmpty(withdraw_id))
                {
                    paras.Add("withdraw_id", withdraw_id);
                }
                String sign = MD5Util.buildMysignV1(paras, this.secret_key);
                paras.Add("sign", sign);
                //发送post请求
                result = httpUtil.requestHttpPost(url_prex, CANCEL_WITHDRAW_RUL,
                        paras);
            }
            catch (Exception e)
            {
                throw e;
            }
            return result;
        }
        /// <summary>
        /// 查询手续费
        /// </summary>
        /// <param name="order_id">订单ID </param>
        /// <param name="symbol">btc_usd:比特币    ltc_usd :莱特币 </param>
        /// <returns></returns>
        public String order_fee(String order_id, String symbol)
        {
            String result = "";
            try
            {
                HttpUtilManager httpUtil = HttpUtilManager.getInstance();
                Dictionary<String, String> paras = new Dictionary<String, String>();
                paras.Add("api_key", api_key);
                if (!StringUtil.isEmpty(symbol))
                {
                    paras.Add("symbol", symbol);
                }
                if (!StringUtil.isEmpty(order_id))
                {
                    paras.Add("order_id", order_id);
                }
                String sign = MD5Util.buildMysignV1(paras, this.secret_key);
                paras.Add("sign", sign);
                //发送post请求
                result = httpUtil.requestHttpPost(url_prex, ORDER_FEE_URL,
                        paras);
            }
            catch (Exception e)
            {
                throw e;
            }
            return result;
        }
        /// <summary>
        ///  获取放款深度前10
        /// </summary>
        /// <param name="symbol">btc_usd: 比特币 ltc_usd: 莱特币 usd: 美元</param>
        /// <returns></returns>
        public String lend_depth(String symbol)
        {
            String result = "";
            try
            {
                HttpUtilManager httpUtil = HttpUtilManager.getInstance();
                Dictionary<String, String> paras = new Dictionary<String, String>();
                paras.Add("api_key", api_key);
                if (!StringUtil.isEmpty(symbol))
                {
                    paras.Add("symbol", symbol);
                }
                String sign = MD5Util.buildMysignV1(paras, this.secret_key);
                paras.Add("sign", sign);
                //发送post请求
                result = httpUtil.requestHttpPost(url_prex, LEND_DEPTH_URL,
                        paras);
            }
            catch (Exception e)
            {
                throw e;
            }
            return result;
        }
        /// <summary>
        ///  查询用户借款信息
        /// </summary>
        /// <param name="symbol">btc_usd: 比特币 ltc_usd: 莱特币 usd: 美元 </param>
        /// <returns></returns>
        public String borrows_info(String symbol)
        {
            String result = "";
            try
            {
                HttpUtilManager httpUtil = HttpUtilManager.getInstance();
                Dictionary<String, String> paras = new Dictionary<String, String>();
                paras.Add("api_key", api_key);
                if (!StringUtil.isEmpty(symbol))
                {
                    paras.Add("symbol", symbol);
                }
                String sign = MD5Util.buildMysignV1(paras, this.secret_key);
                paras.Add("sign", sign);
                //发送post请求
                result = httpUtil.requestHttpPost(url_prex, BORROWS_INFO_URL,
                        paras);
            }
            catch (Exception e)
            {
                throw e;
            }
            return result;
        }
        /// <summary>
        /// 申请借款
        /// </summary>
        /// <param name="symbol">btc_usd: 比特币 ltc_usd: 莱特币 usd: 美元 </param>
        /// <param name="days">借款天数， three，seven，fifteen，thirty，sixty，ninety </param>
        /// <param name="amount">借入数量 </param>
        /// <param name="rate">借款利率 [0.0001, 0.01] </param>
        /// <returns></returns>
        public String borrow_money(String symbol, String days, String amount, String rate)
        {
            String result = "";
            try
            {
                HttpUtilManager httpUtil = HttpUtilManager.getInstance();
                Dictionary<String, String> paras = new Dictionary<String, String>();
                paras.Add("api_key", api_key);
                if (!StringUtil.isEmpty(symbol))
                {
                    paras.Add("symbol", symbol);
                }
                if (!StringUtil.isEmpty(days))
                {
                    paras.Add("days", days);
                }
                if (!StringUtil.isEmpty(amount))
                {
                    paras.Add("amount", amount);
                }
                if (!StringUtil.isEmpty(rate))
                {
                    paras.Add("rate", rate);
                }
                String sign = MD5Util.buildMysignV1(paras, this.secret_key);
                paras.Add("sign", sign);
                //发送post请求
                result = httpUtil.requestHttpPost(url_prex, BORROW_MONEY_URL,
                        paras);
            }
            catch (Exception e)
            {
                throw e;
            }
            return result;
        }
        /// <summary>
        /// 取消借款申请
        /// </summary>
        /// <param name="symbol">btc_usd: 比特币 ltc_usd: 莱特币 usd: 美元 </param>
        /// <param name="borrow_id">借款单ID</param>
        /// <returns></returns>
        public String cancel_borrow(String symbol, String borrow_id)
        {
            String result = "";
            try
            {
                HttpUtilManager httpUtil = HttpUtilManager.getInstance();
                Dictionary<String, String> paras = new Dictionary<String, String>();
                paras.Add("api_key", api_key);
                if (!StringUtil.isEmpty(symbol))
                {
                    paras.Add("symbol", symbol);
                }
                if (!StringUtil.isEmpty(borrow_id))
                {
                    paras.Add("borrow_id", borrow_id);
                }
                String sign = MD5Util.buildMysignV1(paras, this.secret_key);
                paras.Add("sign", sign);
                //发送post请求
                result = httpUtil.requestHttpPost(url_prex, CANCEL_BORROW_URL,
                        paras);
            }
            catch (Exception e)
            {
                throw e;
            }
            return result;
        }
        /// <summary>
        ///  获取借款订单记录
        /// </summary>
        /// <param name="borrow_id">借款单ID</param>
        /// <returns></returns>
        public String borrow_order_info(String borrow_id)
        {
            String result = "";
            try
            {
                HttpUtilManager httpUtil = HttpUtilManager.getInstance();
                Dictionary<String, String> paras = new Dictionary<String, String>();
                paras.Add("api_key", api_key);
                if (!StringUtil.isEmpty(borrow_id))
                {
                    paras.Add("borrow_id", borrow_id);
                }
                String sign = MD5Util.buildMysignV1(paras, this.secret_key);
                paras.Add("sign", sign);
                //发送post请求
                result = httpUtil.requestHttpPost(url_prex, BORROW_ORDER_INFO,
                        paras);
            }
            catch (Exception e)
            {
                throw e;
            }
            return result;
        }
        /// <summary>
        /// 用户还全款
        /// </summary>
        /// <param name="borrow_id">借款单ID</param>
        /// <returns></returns>
        public String repayment(String borrow_id)
        {
            String result = "";
            try
            {
                HttpUtilManager httpUtil = HttpUtilManager.getInstance();
                Dictionary<String, String> paras = new Dictionary<String, String>();
                paras.Add("api_key", api_key);
                if (!StringUtil.isEmpty(borrow_id))
                {
                    paras.Add("borrow_id", borrow_id);
                }
                String sign = MD5Util.buildMysignV1(paras, this.secret_key);
                paras.Add("sign", sign);
                //发送post请求
                result = httpUtil.requestHttpPost(url_prex, REPAYMENT_URL,
                        paras);
            }
            catch (Exception e)
            {
                throw e;
            }
            return result;
        }
        /// <summary>
        /// 未还款列表
        /// </summary>
        /// <param name="symbol">btc_usd: 比特币 ltc_usd: 莱特币 usd: 美元 </param>
        /// <param name="current_page">当前页数</param>
        /// <param name="page_length">每页数据条数，最多不超过50条</param>
        /// <returns></returns>
        public String unrepayments_info(String symbol, String current_page, String page_length)
        {
            String result = "";
            try
            {
                HttpUtilManager httpUtil = HttpUtilManager.getInstance();
                Dictionary<String, String> paras = new Dictionary<String, String>();
                paras.Add("api_key", api_key);
                if (!StringUtil.isEmpty(symbol))
                {
                    paras.Add("symbol", symbol);
                }
                if (!StringUtil.isEmpty(current_page))
                {
                    paras.Add("current_page", current_page);
                }
                if (!StringUtil.isEmpty(page_length))
                {
                    paras.Add("page_length", page_length);
                }
                String sign = MD5Util.buildMysignV1(paras, this.secret_key);
                paras.Add("sign", sign);
                //发送post请求
                result = httpUtil.requestHttpPost(url_prex, UNREPAYMENTS_INFO_URL,
                        paras);
            }
            catch (Exception e)
            {
                throw e;
            }
            return result;
        }
        /// <summary>
        /// 获取用户提现/充值记录
        /// </summary>
        /// <param name="symbol">btc_usd: 比特币 ltc_usd: 莱特币 usd: 美元</param>
        /// <param name="type">0：充值 1 ：提现 </param>
        /// <param name="current_page">当前页数</param>
        /// <param name="page_length">每页数据条数，最多不超过50条</param>
        /// <returns></returns>
        public String account_records(String symbol, String type, String current_page, String page_length)
        {
            String result = "";
            try
            {
                HttpUtilManager httpUtil = HttpUtilManager.getInstance();
                Dictionary<String, String> paras = new Dictionary<String, String>();
                paras.Add("api_key", api_key);
                if (!StringUtil.isEmpty(symbol))
                {
                    paras.Add("symbol", symbol);
                }
                if (!StringUtil.isEmpty(type))
                {
                    paras.Add("type", type);
                }
                if (!StringUtil.isEmpty(current_page))
                {
                    paras.Add("current_page", current_page);
                }
                if (!StringUtil.isEmpty(page_length))
                {
                    paras.Add("page_length", page_length);
                }
                String sign = MD5Util.buildMysignV1(paras, this.secret_key);
                paras.Add("sign", sign);
                //发送post请求
                result = httpUtil.requestHttpPost(url_prex, ACCOUNT_RECORDS_URL,
                        paras);
            }
            catch (Exception e)
            {
                throw e;
            }
            return result;
        }
        /// <summary>
        ///  获取历史交易信息
        /// </summary>
        /// <param name="symbol">btc_usd:比特币 ltc_usd :莱特币 </param>
        /// <param name="since">从某一tid开始访问600条数据(必填项) </param>
        /// <returns></returns>
        public String trade_history(String symbol, String since)
        {
            String result = "";
            try
            {
                HttpUtilManager httpUtil = HttpUtilManager.getInstance();
                Dictionary<String, String> paras = new Dictionary<String, String>();
                paras.Add("api_key", api_key);
                if (!StringUtil.isEmpty(symbol))
                {
                    paras.Add("symbol", symbol);
                }
                if (!StringUtil.isEmpty(since))
                {
                    paras.Add("since", since);
                }
                String sign = MD5Util.buildMysignV1(paras, this.secret_key);
                paras.Add("sign", sign);
                //发送post请求
                result = httpUtil.requestHttpPost(url_prex, TRADE_HISTORY_URL,
                        paras);
            }
            catch (Exception e)
            {
                throw e;
            }
            return result;
        }
    }
}
