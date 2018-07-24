# *- coding:utf-8 *-
import sys
import os

sys.path.append(os.path.dirname(os.getcwd()))

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, create_engine, Integer, String, Text, Float
from ManagerSystem.config import dbconfig as cfg

DB_PARAMS = "{0}://{1}:{2}@{3}/{4}?charset={5}".format(
    cfg.sqlenginename, cfg.username, cfg.password, cfg.host, cfg.database, cfg.charset)
mysql_engine = create_engine(DB_PARAMS, echo=False)
Base = declarative_base()


class Users(Base):
    __tablename__ = "Users"
    USid = Column(String(64), primary_key=True)
    UStelphone = Column(String(14), nullable=False)  # 用户联系方式
    USpassword = Column(String(32), nullable=False)  # 用户密码
    USname = Column(String(64))                      # 用户昵称
    USsex = Column(Integer)                          # 用户性别 {101男， 102女}
    UScoin = Column(Float)                           # 用户积分，根据用户购买商品生成
    USinvate = Column(String(64))                    # 用户邀请码，算法生成待设计
    UScreateTime = Column(String(14))
    USloginTime = Column(String(14))
    USstatus = Column(Integer)


class Locations(Base):
    __tablename__ = "Locations"
    LOid = Column(String(64), primary_key=True)
    LOtelphone = Column(String(14), nullable=False)  # 收件人联系方式
    LOname = Column(String(128), nullable=False)     # 收件人姓名
    LOno = Column(String(8), nullable=False)         # 邮编
    LOdetail = Column(Text, nullable=False)          # 收件人详细地址
    LOprovince = Column(String(64), nullable=False)  # 收件人省份
    LOcity = Column(String(64), nullable=False)      # 收件人城市
    LOarea = Column(String(64), nullable=False)      # 收件人城区
    LOisedit = Column(Integer, nullable=False)       # 是否可编辑 {301:可编辑,302:不可编辑,303:已删除}
    USid = Column(String(64), nullable=False)        # 用户id


class Review(Base):
    __tablename__ = "Review"
    REid = Column(String(64), primary_key=True)  # 评论id
    PRid = Column(String(64), nullable=False)    # 对应的评论对象，根据REtype判断
    USid = Column(String(64), nullable=False)    # 用户id
    REtime = Column(String(14), nullable=False)  # 评论时间
    USRid = Column(String(64))                   # 被评论人
    REcontent = Column(Text, nullable=True)      # 评价内容
    REtype = Column(Integer, default=1)          # 对应的评论对象类型 {701:商品评价 702:帖子评价}


# 商品
class Products(Base):
    __tablename__ = "Products"
    PRid = Column(String(64), primary_key=True)  # 商品id
    PRname = Column(String(64), nullable=False)  # 商品名称
    PRvideo = Column(Text, nullable=False)       # 宣传视频
    PRimage = Column(Text, nullable=False)       # 商品图片存放地址
    PRaboimage = Column(Text)                    # 商品详情图存放地址
    PRinfo = Column(Text)                        # 商品介绍
    PRtype = Column(Integer, nullable=False)     # 营销类型 {501自营， 502非自营}
    PRbrand = Column(Text, nullable=False)    # 类目 {601美妆类， 602 3C类}
    PRvideostart = Column(Text)                  # 商品视频未启动图片
    MAid = Column(String(64))                    # 商家id
    PRtime = Column(String(14))                  # 创建时间
    CTid = Column(String(64))                    # 类目id
    PRfranking = Column(Float)                   # 邮费
    PRPoint = Column(Text)


class ProductsBrands(Base):
    __tablename__ = "ProductsBrands"
    PBid = Column(String(64), primary_key=True)
    PRid = Column(String(64), nullable=False)        # 商品id
    BRid = Column(String(64), nullable=False)        # 叶子类目id
    PBprice = Column(Float, nullable=Float)          # 商品价格
    PBunit = Column(Integer, nullable=False)         # 货币单位 {401美元， 402人民币， 403欧元， 404英镑}
    PBstatus = Column(Integer, default=201)          # 商品状态 {201:在售状态 202:下架状态, 203: 预售}
    PBsalesvolume = Column(Integer, nullable=False)  # 商品销量
    PBscore = Column(Float, nullable=True)           # 商品评分
    PBimage = Column(Text, nullable=False)           # 商品图片存放地址
    PBmarkingPrice = Column(Float)                   # 商品划线价格


class Brands(Base):
    __tablename__ = "Brands"
    BRid = Column(String(64), primary_key=True)
    BRfromid = Column(String(64), nullable=False)  # 父节点id，如果没有父节点则为0
    BRvalue = Column(String(128), nullable=False)  # 属性值
    BRkey = Column(String(128), nullable=False)    # 属性类型


class Category(Base):
    __tablename__ = "Category"
    CTid = Column(String(64), primary_key=True)    # 主键
    CTname = Column(Text)                          # 类目简称
    CTfromid = Column(String(64))                  # 类目父id
    MAid = Column(String(64))                      # 创建人id


class CategoryBrand(Base):
    __tablename__ = "Categorybrand"
    CBid = Column(String(64), primary_key=True)
    CTid = Column(String(64))
    CBname = Column(String(64))
    CBvalue = Column(Text)


# 库存
class Stocks(Base):
    __tablename__ = "Stocks"
    STid = Column(String(64), primary_key=True)
    STname = Column(Text)
    STamount = Column(Integer, default=0)
    STabo = Column(Text)


class StocksProducts(Base):
    __tablename__ = "StocksProducts"
    SPid = Column(String(64), primary_key=True)
    STid = Column(String(64))
    PBid = Column(String(64))
    PBnumber = Column(Integer)


# 订单
class OrderMain(Base):
    __tablename__ = "OrderMain"
    OMid = Column(String(64), primary_key=True)         # 主订单id
    OMtime = Column(String(14), nullable=False)         # 下单时间
    OMstatus = Column(Integer, nullable=False)          # 订单状态 具体状态如下：
    # {0 : 已取消, 7 : 未支付, 14 : 支付中, 21: 已支付, 28: 已发货, 35: 已收货, 42 : 已完成,  49 : 已评价}
    OMprice = Column(Float)                             # 订单总额
    USid = Column(String(64))                           # 用户id
    LOid = Column(String(64))                           # 配送地址id
    OMlogisticsName = Column(Text, default="顺丰速运")    # 物流公司
    OMabo = Column(Text)                                # 订单备注
    OMcointype = Column(Integer, nullable=False)        # 货币单位 {401美元， 402人民币， 403欧元， 404英镑}
    COid = Column(String(64))                           # 优惠券id


class Orderpart(Base):
    __tablename__ = "OrderPart"
    OPid = Column(String(64), primary_key=True)  # 分订单id
    OMid = Column(String(64), nullable=False)    # 主订单id
    PBid = Column(String(64), nullable=False)    # 商品id
    PRnumber = Column(Integer, nullable=False)   # 商品数量


class Coupons(Base):
    __tablename__ = "Coupon"
    COid = Column(String(64), primary_key=True)
    COfilter = Column(Float)      # 优惠券优惠条件，到达金额
    COdiscount = Column(Float)    # 折扣，值为0-1，其中0为免单
    COamount = Column(Float)      # 优惠金额，减免金额，限制最大数目
    CObrand = Column(String(64))  # 商品类别，限制部分商品使用
    COstart = Column(String(14))  # 优惠券的开始时间
    COend = Column(String(14))    # 优惠券的结束时间
    COutype = Column(Integer)     # 优惠券限制的使用人群，用于后期扩展会员
    COtype = Column(Integer)      # 优惠券类型 {801 满减， 802 满折， 803 商品类目限制， 804 无限制， 805 用户类型限制， 806: 店铺折扣}
    MAid = Column(String(64))     # 店家id
    PRid = Column(Text)           # 商品id


# 活动
class Actives(Base):
    __tablename__ = "Actives"
    ACid = Column(String(64), primary_key=True)
    MAid = Column(String(64))     # 店家id
    ACabo = Column(Text)          # 活动详情
    ACimage = Column(Text)        # 活动宣传图画
    ACstart = Column(String(14))  # 活动开始时间
    ACend = Column(String(14))    # 活动结束时间
    ACfilter = Column(Float)
    ACdiscount = Column(Float)    # 折扣，值为0-1，其中0为免单
    ACamount = Column(Float)      # 优惠金额，减免金额，限制最大数目
    ACbrand = Column(String(64))  # 商品类别，限制部分商品使用
    ACtype = Column(Integer)      # 优惠券类型 {801 满减， 802 满折， 803 商品类目限制， 804 无限制， 805 用户类型限制， 806: 店铺折扣}
    PRid = Column(Text)           # 商品id


# 用户
class Manager(Base):
    __tablename__ = "Manager"
    MAid = Column(String(64), primary_key=True)
    MAname = Column(String(64))                       # 用户名
    MAnicname = Column(String(64))                    # 昵称
    MAtelphone = Column(String(14))                   # 管理员联系方式
    MAemail = Column(Text)                            # 管理员邮箱
    MAidentity = Column(Integer, nullable=False)      # 管理员身份
    # {100: 超级管理员, 101: 管理员, 102: 一级分销商, 103: 二级分销商, 104: 三级分销商, 105: 卖家}
    MApassword = Column(String(64), nullable=False)       # 管理员密码
    MAstatus = Column(Integer, nullable=False)        # 账号状态 {151: 可用，152: 禁用, 153: 未激活}
    MAcreatTime = Column(String(14), nullable=False)  # 账号创建时间
    MAendTime = Column(String(14))                    # 账号到期时间
    MAidNumber = Column(String(18))                   # 法人身份证号码
    MAidImageFront = Column(Text)                     # 法人身份证A面
    MAidImageReverse = Column(Text)                   # 法人身份证B面
    MAbusinessLicense = Column(Text)                  # 店家营业执照
    MAcredit = Column(String(18))                     # 统一社会信用代码
    MAloginTime = Column(String(14))                  # 最后一次登录时间


# 权限
class Permission(Base):
    __tablename__ = "Permission"
    PEid = Column(String(64), primary_key=True)
    PEname = Column(String(64), nullable=False)   # 权限名称
    MAid = Column(String(64), nullable=False)     # 店家id
    PEtype = Column(Integer, nullable=False)      # 审批类型
    # {204: 商品发布审批, 201: 成为卖家审批, 202: 类目使用审批, 203 类目增设审批, 204: 活动发起审批}
    PEsubLevel = Column(Integer, nullable=False)  # 审批层级 1-10


class Menu(Base):
    __tablename__ = "Menu"
    MNid = Column(String(64), primary_key=True)
    MNname = Column(String(66))    # 菜单名称
    MNurl = Column(String(255))    # 菜单url
    MNicon = Column(String(255))          # 菜单图标名称
    MNparent = Column(String(64))  # 父菜单节点id，根节点为0


class Element(Base):
    __tablename__ = "Element"
    ELid = Column(String(64), primary_key=True)
    ELname = Column(String(255), nullable=False)  # 页面元素名称


class ManagerMenu(Base):
    __tablename__ = "ManagerMenu"
    MMid = Column(String(64), primary_key=True)
    MAid = Column(String(64))  # 店家id
    MNid = Column(String(64))  # 菜单子节点id


class ManagerElement(Base):
    __tablename__ = "ManagerElement"
    MEid = Column(String(64),primary_key=True)
    MAid = Column(String(64), nullable=False)  # 店家id
    ELid = Column(String(64), nullable=False)  # 页面元素id


# 审批流
class Approval(Base):
    __tablename__ = "Approval"
    APid = Column(String(64), primary_key=True)
    APname = Column(Text)    # 审批名称
    APremark = Column(Text)  # 审批备注
    APstart = Column(String(64))     # 发起人id
    APreceive = Column(String(64))   # 当前审批人id
    APstatus = Column(Integer)       # 审批状态 {411: 发起, 412: 审批中, 413: 审批结束，414: 拒绝}
    PEtype = Column(Integer)         # 审批类型
    APtime = Column(String(14))      # 发起时间
    APcontent = Column(String(64))   # 待审批活动/商品/类目


# 修改密码所用的验证码
class IdentifyingCode(Base):
    __tablename__ = "IdentifyingCode"
    ICid = Column(String(64), primary_key=True)         # 主键
    ICtelphone = Column(String(14), nullable=False)     # 获取验证码的手机号
    ICcode = Column(String(8), nullable=False)          # 获取到的验证码
    ICtime = Column(String(14), nullable=False)         # 获取的时间


# 黑名单
class BlackUsers(Base):
    __tablename__ = "BlackUsers"
    BUid = Column(String(64), primary_key=True)         # 主键
    BUtelphone = Column(String(14), nullable=False)     # 黑名单电话
    BUreason = Column(Text)                             # 加入黑名单的原因

