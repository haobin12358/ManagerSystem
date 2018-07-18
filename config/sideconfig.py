# *- coding:utf-8 *-

side = {
  "side":[
    {
      "MNname":"用户权限",
      "MNurl":"/jurisdiction",
      "MNicon":"icon-person-side",
      "children":[
        {
          "MNname":"管理员管理",
          "MNurl":"admin",
          "MNicon":"none"
        },
        {
          "MNname":"用户数据管理",
          "MNurl":"user",
          "MNicon":"none"
        }
      ]
    },
    {
      "MNname":"产品管理",
      "MNurl":"/commodity",
      "MNicon":"icon-product",
      "children":[
        {
          "MNname":"商品管理",
          "MNurl":"commodityManagement",
          "MNicon":"none"
        },
        {
          "MNname":"商品发布",
          "MNurl":"categorySelection",
          "MNicon":"none"
        },
        {
          "MNname":"商品分组",
          "MNurl":"commodityGroup",
          "MNicon":"none"
        }
      ]
    },
    {
      "MNname":"订单管理",
      "MNurl":"/order",
      "MNicon":"icon-order",
      "children":[
        {
          "MNname":"订单概况",
          "MNurl":"orderIndex",
          "MNicon":"none"
        },
        {
          "MNname":"所有订单",
          "MNurl":"allOrder",
          "MNicon":"none"
        },
        {
          "MNname":"退款维权",
          "MNurl":"refund",
          "MNicon":"none"
        }
      ]
    },
    {
      "MNname":"活动中心",
      "MNurl":"/activity",
      "MNicon":"icon-activity",
      "children":[
        {
          "MNname":"单品活动",
          "MNurl":"productActivity",
          "MNicon":"none"
        },
        {
          "MNname":"店铺活动",
          "MNurl":"storeActivity",
          "MNicon":"none"
        },
        {
          "MNname":"优惠券",
          "MNurl":"discountCoupon",
          "MNicon":"none"
        }
      ]
    }
  ]
}


if __name__ == "__main__":
  from ManagerSystem.service.SInterface import SInterface
  sint = SInterface()
  menu = side.get("side")
  import uuid
  def add_menu(parentid, menu_list):
    for menu_item in menu_list:
      MNid = str(uuid.uuid1())
      if menu_item.get("children"):
        add_menu(MNid, menu_item.pop("children"))
      menu_item["MNid"] = MNid
      menu_item["MNparent"] = parentid
      sint.add_model("Menu", **menu_item)

  add_menu("0", menu)