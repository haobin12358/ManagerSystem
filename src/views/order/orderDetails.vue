<template>
  <div class="m-step">
    <page-title :title="name" @freshClick="freshClick"></page-title>
    <div class="m-step-content">
      <div class="m-step-part">
        <step :list="step"></step>
      </div>
      <div class="details-middle-left">
        <div class="m-step-part">
          <h4>订单详情</h4>
          <div class="order-info-part">
            <div class="left-text-div">
              <div class="left-text" style="margin-top: 0.1rem">订单编号：</div>
              <div class="left-text">付款方式：</div>
              <div class="left-text" style="margin-left: 0.38rem;">买 家：</div>
              <div class="left-text">配送方式：</div>
              <div class="left-text">收货地址：</div>
              <div class="left-text" style="margin-top: 0.25rem">买家留言：</div>
            </div>
            <div class="left-value-div">
              <div class="left-text" style="margin-top: 0.1rem">{{order.orderNo}}</div>
              <div class="left-text">{{order.payType}}</div>
              <div class="left-text">{{order.buyer}}</div>
              <div class="left-text">{{order.sendType}}</div>
              <div class="left-text">{{order.buyerAddress}}</div>
              <div class="left-text" style="margin-top: 0.25rem">{{order.memo}}</div>
            </div>
          </div>
        </div>
      </div>
      <div class="details-middle-right">
        <div class="m-step-part">
          <div class="right-top-top">
            <div class="left-icon"><img src="../../assets/images/toSend.png" height="50"/></div>
            <div class="right-text">
              <div class="right-top">订单状态：买家已付款，等待卖家发货</div>
              <div class="right-bottom">买家已付款至待结算账户，请尽快发货，否则买家有权利申请退款</div>
            </div>
          </div>
          <div class="right-middle">
            <el-dialog title="收货地址" :visible.sync="toSendForm" style="padding: 0">
              <div class="buyer-info">
                <div class="buyer-info-title">买家收货信息</div>
                <div class="info-left-text-div">
                  <div class="info-text">订单ID：</div>
                  <div class="info-text">买家昵称：</div>
                  <div class="info-text">收货人：</div>
                  <div class="info-text">收货地址：</div>
                  <div class="info-text">联系电话：</div>
                  <div class="info-text">备注：</div>
                </div>
                <div class="info-right-text-div">
                  <div class="info-text-value">{{order.orderNo}}</div>
                  <div class="info-text-value">{{order.buyer}}</div>
                  <div class="info-text-value">{{order.buyer}}</div>
                  <div class="info-text-value">{{order.buyerAddress}}</div>
                  <div class="info-text-value">{{order.payNo}}</div>
                  <div class="info-text-value">{{order.memo}}</div>
                </div>
              </div>
              <div class="send-info">
                <el-form :model="form" class="send-info-form">
                  <el-form-item label="物流公司:" :label-width="formLabelWidth">
                    <el-select v-model="form.region" placeholder="" style="width: 1.7rem" size="small">
                      <el-option label="圆通快递" value="shanghai"></el-option>
                      <el-option label="中通快递" value="beijing"></el-option>
                    </el-select>
                  </el-form-item>
                  <el-form-item label="快递单号:" :label-width="formLabelWidth">
                    <el-input v-model="form.name" auto-complete="off" style="width: 1.7rem" size="small"></el-input>
                  </el-form-item>
                </el-form>
              </div>
              <div slot="footer" style="text-align: center;margin-bottom: 0.2rem">
                <el-button class="right-button" style="background-color: #fff;color: #000" @click="toSendForm = false">取 消</el-button>
                <el-button class="right-button" @click="toSend">确 定</el-button>
              </div>
            </el-dialog>
            <el-dialog title="备 注" :visible.sync="memoForm">
              <el-form :model="memoForms">
                <el-form-item label="备 注：" :label-width="formLabelWidth">
                  <el-input v-model="memoForms.name" auto-complete="off" size="small" type="textarea" :autosize="{ minRows: 2, maxRows: 4}"></el-input>
                </el-form-item>
              </el-form>
              <div slot="footer" class="dialog-footer">
                <el-button class="right-button" style="background-color: #fff;color: #000" @click="memoForm = false">取 消</el-button>
                <el-button class="right-button" @click="memoForm = false">确 定</el-button>
              </div>
            </el-dialog>
            <el-button class="right-button" @click="toSendForm=true">发 货</el-button>
            <el-button class="right-button" @click="" style="margin-left: 0.2rem;" @click="memoForm=true">备 注</el-button>
          </div>
          <div class="right-bottom-text">
            <div class="bottom-title">温馨提示</div>
            <div class="bottom-text">•如果无法发货，请及时与买家联系并说明情况后进行退款；</div>
            <div class="bottom-text">•买家申请退款后，需征得卖家同意后再发货，否则卖家有权拒收货物；</div>
            <div class="bottom-text">•买家付款后超过7天仍未发货，将有权申请平台客服介入发起退款维权。</div>
          </div>
        </div>
      </div>
      <div class="details-bottom">
        <div class="bottom-total">订单共计4件商品，总计：159.00元（含运费￥0.00元）</div>
        <el-table class="details-table" :data="order.goods" border style="width: 100%" stripe size="mini">
          <el-table-column align="center" prop="goodsName" label="商品">
          </el-table-column>
          <el-table-column align="center" prop="goodsPrice" label="价格（元）">
          </el-table-column>
          <el-table-column align="center" prop="goodsNumber" label="数量">
          </el-table-column>
          <el-table-column align="center" prop="afterSales" label="优惠">
          </el-table-column>
          <el-table-column align="center" prop="realPay" label="小计">
          </el-table-column>
        </el-table>
      </div>
    </div>
  </div>
</template>

<script>
  // 1、待付款，2、待发货，3、已发货，4、已完成，5、已关闭，6、退款中
  import allOrder from "../../common/json/allOrder";
  import pageTitle from '../../components/common/title';
  import step from '../../components/common/step';
  export default {
    name: "orderDetails",
    data() {
      return {
        name: '所有订单 > 订单详情',
        order: '',
        step:[
          {
            name:'买家下单',
            time: '2018-07-12 14:25:20',
            active:true,
            next:true
          },
          {
            name:'买家付款',
            time: '2018-07-12 14:34:21',
            active:true,
            next:true
          },
          {
            name:'商家发货',
            time: '待发货',
            active:false,
            next:false
          },
          {
            name:'交易完成',
            time: '未完成',
            active:false,
            next:false
          }
        ],
        star: 0,
        toSendForm: false,
        memoForm: false,
        form: {
          name: '',
          region: ''
        },
        memoForms: {
          name: ''
        },
        formLabelWidth: '0.6rem'
      }
    },
    components: {
      'pageTitle': pageTitle,
      'step': step
    },
    methods: {
      freshClick(){
        console.log('fresh');
      },
      toSend() {
        this.toSendForm = false
        this.step = [
          {
            name:'买家下单',
            time: '2018-07-12 14:25:20',
            active:true,
            next:true
          },
          {
            name:'买家付款',
            time: '2018-07-12 14:34:37',
            active:true,
            next:true
          },
          {
            name:'商家发货',
            time: '2018-07-13 10:20:05',
            active:false,
            next:false
          },
          {
            name:'交易完成',
            time: '未完成',
            active:false,
            next:false
          }
        ]
      }
    },
    created() {
      this.order = this.$route.query.order;
      // console.log(this.order)
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/_variate.less";
  @import "../../common/css/activity";
  .m-step {
    .m-step-content {
      .el-button--primary {
       background-color: #ef636e;
      }
      /*height: 5rem;*/
      .details-middle-left {
        width: 40%;
        float: left;
        .order-info-part {
          height: 2.05rem;
          .left-text-div {
            width: 20%;
            float: left;
          }
          .left-value-div {
            width: 80%;
            float: right;
          }
          .left-text {
            font-size: 14px;
            color: @greyColor;
            line-height: 0.12rem;
            margin: 0 0 0.15rem 0.2rem;
          }
        }
      }
      .details-middle-right {
        width: 58%;
        float: right;
        .m-step-part {
          .right-top-top {
            padding: 0.1rem;
            .left-icon {
              width: 10%;
              float: left;
              margin-left: 10px;
              margin-top: 10px;
            }
            .right-text {
              width: 85%;
              float: left;
              .right-top {
                font-size: 18px;
                font-weight:bold;
                margin-bottom: 20px;
              }
            }
          }
          .right-middle {
            margin: 0.7rem 0.8rem 0.14rem 0.8rem;
            .right-button {
              width: 0.8rem;
              height: 0.3rem;
              font-size: 14px;
              background-color: @btnActiveColor;
              color: @bgMainColor;
            }
            .buyer-info {
              width: 50%;
              float: left;
              margin: 0 0.2rem 0.2rem 0.2rem;
              border: 1px solid @borderColor;
              border-radius: 5px;
              .buyer-info-title {
                margin: 0 0 0.15rem 0.15rem;
                font-size: 18px;
                color: @red;
              }
              .info-left-text-div {
                width: 20%;
                float: left;
              }
              .info-right-text-div {
                width: 80%;
                float: right;
              }
              .info-text {
                text-align: right;
                font-size: 14px;
                color: @greyColor;
                line-height: 0.12rem;
                margin: 0 0 0.05rem 0.1rem;
              }
              .info-text-value {
                text-align: left;
                font-size: 14px;
                color: @greyColor;
                line-height: 0.12rem;
                margin: 0 0 0.05rem 0.1rem;
              }
            }
            .send-info-form {
              width: 40%;
              float: right;
              padding: 1% 3% 0 0;
            }
          }
          .right-bottom-text {
            padding: 0.2rem;
            .bottom-title {
              color: @red;
              font-size: 16px;
              margin-bottom: 0.1rem;
            }
            .bottom-text {
              font-size: 14px;
              color: @greyColor;
              margin-top: 0.05rem;
            }
          }
        }
      }
      .details-bottom {
        .bottom-total {
          float: right;
          font-size: 16px;
          margin-bottom: 0.1rem;
        }
      }
    }
  }
</style>
