# *- coding:utf8 *-
conversion_PBunit = {401: "$", 402: "￥", 403: "欧元", 404: "英镑"}
conversion_PRtype = {501: "自营", 502: "非自营"}
conversion_PRbrand = {601: "美妆类", 602: "3C类"}
conversion_PBstatus = {201: "在售状态", 202: "下架状态", 203: "预售状态", 204: "未发布", 207: "删除状态", 205: "发布中"}
conversion_OMstatus = {0: "已取消", 7: "未支付", 14: "支付中", 21: "已支付",
                       28: "已发货", 35: "已收货", 42: "已完成", 49: "已评价"}
conversion_COtype = {801: "满减", 802: "满折", 803: "商品类目限制", 804: "无限制", 805: "用户类型限制"}
conversion_MAidentity = {100: "超级管理员", 101: "管理员", 102: "一级分销商",
                         103: "二级分销商", 104: "三级分销商", 105: "卖家"}
conversion_MAstatus = {151: "可用", 152: "禁用", 153: "未激活"}
conversion_PEtype = {301: "成为卖家审批", 302: "类目使用审批",
                     303: "类目增设审批", 304: "商品发布审批", 305: "活动发起审批"}

# value 和 key 转置的dict
conversion_OMstatus_reverse = {v: k for k, v in conversion_OMstatus.items()}
conversion_PBunit_reverse = {v: k for k, v in conversion_PBunit.items()}
conversion_PRtype_reverse = {v: k for k, v in conversion_PRtype.items()}
conversion_PRbrand_reverse = {v: k for k, v in conversion_PRbrand.items()}
conversion_PBstatus_reverse = {v: k for k, v in conversion_PBstatus.items()}
conversion_MAidentity_reverse = {v: k for k, v in conversion_MAidentity.items()}
conversion_MAstatus_resverse = {v: k for k, v in conversion_MAstatus.items()}
conversion_PEtype_resverse = {v: k for k, v in conversion_PEtype.items()}

MTR = 1 / 6.3753
RTM = 1 / 0.1569
MTO = 1 / 0.8492
OTM = 1 / 1.1776
MTY = 1 / 0.7424
YTM = 1 / 1.347
RTO = 1 / 0.1332
OTR = 1 / 7.5082
RTY = 1 / 0.1163
YTR = 1 / 8.5958
OTY = 1 / 0.8742
YTO = 1 / 1.1439
