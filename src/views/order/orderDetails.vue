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
              <div class="left-text">订单编号：</div>
              <div class="left-text">订单状态：</div>
              <div class="left-text" style="margin-left: 0.38rem;">买 家：</div>
              <div class="left-text">联系方式：</div>
              <div class="left-text">快递方式：</div>
              <div class="left-text">收货地址：</div>
              <div class="left-text">买家留言：</div>
            </div>
            <div class="left-value-div">
              <div class="left-text">{{order.OMid}}</div>
              <div class="left-text">{{order.OMstatus}}</div>
              <div class="left-text">{{order.LOname}}</div>
              <div class="left-text">{{order.LOtelphone}}</div>
              <div class="left-text">{{order.OMlogisticsName}}</div>
              <div class="left-text">{{order.LOdetail}}</div>
              <div class="left-text">{{order.OMabo}}</div>
            </div>
          </div>
        </div>
      </div>
      <div class="details-middle-right">
        <div class="m-step-part">
          <div class="right-top-top">
            <div class="left-icon"><img src="../../assets/images/toSend.png" height="50"/></div>
            <div class="right-text">
              <div class="right-top">订单状态：{{orderStatus}}</div>
              <!--<div class="right-bottom">{{reminder}}</div>-->
            </div>
          </div>
          <div class="right-middle">
            <!--发货弹出框-->
            <el-dialog title="收货地址" :visible.sync="toSendForm" style="padding: 0">
              <div class="buyer-info">
                <div class="buyer-info-title">买家收货信息</div>
                <div class="info-left-text-div">
                  <div class="info-text">订单编号：</div>
                  <div class="info-text">联系对象：</div>
                  <div class="info-text">联系方式：</div>
                  <div class="info-text">收货地址：</div>
                  <div class="info-text">下单时间：</div>
                  <div class="info-text">备注：</div>
                </div>
                <div class="info-right-text-div">
                  <div class="info-text-value">{{order.OMid}}</div>
                  <div class="info-text-value">{{order.LOname}}</div>
                  <div class="info-text-value">{{order.LOtelphone}}</div>
                  <div class="info-text-value">{{order.LOdetail}}</div>
                  <div class="info-text-value">{{order.OMtime}}</div>
                  <div class="info-text-value">{{order.OMabo}}</div>
                </div>
              </div>
              <div class="send-info">
                <el-form :model="form" class="send-info-form">
                  <el-form-item label="物流公司:" :label-width="formLabelWidth">
                    <el-select v-model="form.region" placeholder="" style="width: 1.7rem" size="small">
                      <el-option label="顺丰速运" value="顺丰速运"></el-option>
                      <el-option label="EMS" value="EMS"></el-option>
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
            <!--备注弹出框-->
            <el-dialog title="备 注" :visible.sync="memoForm" width="4rem">
              <el-form :model="memoForms">
                <el-form-item label="备 注：" :label-width="formLabelWidth">
                  <el-input v-model="memoForms.name" auto-complete="off" size="small" type="textarea" :autosize="{ minRows: 2, maxRows: 5}" style="width: 90%"></el-input>
                </el-form-item>
              </el-form>
              <div slot="footer" class="dialog-footer">
                <el-button class="right-button" style="background-color: #fff;color: #000" @click="memoForm = false">取 消</el-button>
                <el-button class="right-button" @click="memoForm = false">确 定</el-button>
              </div>
            </el-dialog>
            <!--显示物流信息弹出框-->
            <el-dialog title="物流信息" :visible.sync="searchWhere" width="4rem">
              <div v-for="where in whereList" class="where-list">
                {{where}}
              </div>
              <span slot="footer" class="dialog-footer">
                <el-button class="right-button" @click="searchWhere=false">确 定</el-button>
              </span>
            </el-dialog>
            <!--判断订单状态后显示相应的操作按钮-->
            <div v-if="order.OMstatus=='已取消'">
              <div style="height: 0.3rem">用户已取消订单</div>
            </div>
            <div v-if="order.OMstatus=='未支付'">
              <div style="height: 0.3rem">等待用户支付</div>
            </div>
            <div v-if="order.OMstatus=='支付中'">
              <div style="height: 0.3rem">等待支付款项到账</div>
            </div>
            <div v-if="order.OMstatus=='已支付'">
              <el-button class="right-button" @click="toSendForm=true">发 货</el-button>
              <!--<el-button class="right-button" @click="" style="margin-left: 0.2rem;" @click="memoForm=true">备 注</el-button>-->
            </div>
            <div v-if="order.OMstatus=='已发货'">
              <el-button class="right-button" @click="searchWhere=true">查看物流进度</el-button>
            </div>
            <div v-if="order.OMstatus=='已收货'">
              <div style="height: 0.3rem">用户已收货</div>
            </div>
            <div v-if="order.OMstatus=='已完成'">
              <div style="height: 0.3rem">该订单已完成</div>
            </div>
            <div v-if="order.OMstatus=='已评价'">
              <div style="height: 0.3rem">用户已评价该订单</div>
            </div>
            <div v-if="order.OMstatus=='退款中'">
              <div style="height: 0.3rem">该订单正在退款中</div>
            </div>
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
        <div class="bottom-total">总计：{{order.OMprice}}元</div>
        <el-table class="details-table" :data="order.order_abo" border style="width: 100%" stripe size="mini">
          <el-table-column align="center" prop="PBimage" label="商品图片">
            <template slot-scope="scope">
              <img  :src="scope.row.PBimage" alt="" style="width: 0.5rem;height: 0.5rem">
            </template>
          </el-table-column>
          <el-table-column align="center" prop="PRname" label="商品名称">
          </el-table-column>
          <el-table-column align="center" prop="PBprice" label="单价">
          </el-table-column>
          <el-table-column align="center" prop="PRnumber" label="数量">
          </el-table-column>
          <el-table-column align="center" prop="PRinfo" label="商品简介">
          </el-table-column>
          <el-table-column align="center" prop="PRtype" label="商品类型">
          </el-table-column>
          <el-table-column align="center" prop="PRbrand" label="商品分类">
          </el-table-column>
        </el-table>
      </div>
    </div>
  </div>
</template>

<script>
  // 0: "已取消", 7: "未支付", 14: "支付中", 21: "已支付",28: "已发货", 35: "已收货", 42: "已完成", 49: "已评价", 56: "退款中"
  import allOrder from "../../common/json/allOrder";
  import pageTitle from '../../components/common/title';
  import step from '../../components/common/step';
  import api from '../../api/api';
  import {Message} from 'element-ui';
  import axios from 'axios';
  export default {
    name: "orderDetails",
    data() {
      return {
        name: '所有订单 > 订单详情',
        order: '',
        OMid: '',
        step:[],
        orderStatus: '',
        searchWhere: false,
        whereList: [
          "2018-07-15 14:25:23 快递已到达杭州萧山分拨中心",
          "2018-07-14 14:25:23 快递已到达杭州分拨中心",
          "2018-07-13 14:25:23 快递已到达分拨中心",
          "2018-07-13 14:25:23 快递已到达杭州萧山分拨中心",
          "2018-07-13 14:25:23 快递已到达杭州萧山分拨中心",
          "2018-07-13 14:25:23 快递已到达杭州萧山分拨中心",
          "2018-07-13 14:25:23 快递已到达杭州萧山分拨中心",
          "2018-07-13 14:25:23 快递已到达杭州萧山分拨中心",
          "2018-07-13 14:25:23 快递已到达杭州萧山分拨中心",
          "2018-07-13 14:25:23 快递已到达杭州萧山分拨中心",
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
      // 获取订单详情
      getData(OMid){
        let params = {
          token: localStorage.getItem('token'),
          OMid: OMid
        };
        axios.get(api.get_order_by_LOid,{params:params}).then(res => {
          if(res.data.status == 200) {
            this.order =res.data.data
            // console.log(this.order)
            this.setStep()
          }else{
            this.$message.error(res.data.message);
          }
        },error => {
          this.$message.error(error.data.message);
        })
      },
      // 将已支付的订单发货，使之变成已发货
      toSend() {
        this.toSendForm = false
        if(this.order.OMstatus == '已支付') {
          let token = localStorage.getItem('token')
          let params = {
            OMid: this.order.OMid,
            OMstatus: '已发货'
          }
          axios.post(api.update_order_status+'?token='+token,params).then(res=>{
            if(res.data.status == 200){
              this.order.OMstatus = '已发货'
              this.orderStatus = this.order.OMstatus
              this.setStep()
              this.$message({ message: res.data.message, type: 'success' });
            }else{
              this.$message.error(res.data.message);
            }
          }, res=>{
            this.$message.error(res.data.message);
          });
        }
      },
      // 依据订单状态设置页面上部的step步骤条
      setStep() {
        if(this.order.OMstatus == '已取消') {
          this.step = [
            { name:'买家下单', time: this.order.OMtime, active:true, next:true },
            { name:'买家支付', time: '订单已取消', active:false, next:false },
            { name:'商家发货', time: '订单已取消', active:false, next:false },
            { name:'交易完成', time: '未完成', active:false, next:false }]
          this.orderStatus = this.order.OMstatus
        }else if(this.order.OMstatus == '未支付') {
          this.step = [
            { name:'买家下单', time: this.order.OMtime, active:true, next:true },
            { name:'买家支付', time: '待支付', active:false, next:false },
            { name:'商家发货', time: '待发货', active:false, next:false },
            { name:'交易完成', time: '未完成', active:false, next:false }]
          this.orderStatus = this.order.OMstatus
        }else if(this.order.OMstatus == '支付中') {
          this.step = [
            { name:'买家下单', time: this.order.OMtime, active:true, next:true },
            { name:'买家支付', time: '支付中', active:true, next:true },
            { name:'商家发货', time: '待发货', active:false, next:false },
            { name:'交易完成', time: '未完成', active:false, next:false }]
          this.orderStatus = this.order.OMstatus
        }else if(this.order.OMstatus == '已支付') {
          this.step = [
            { name:'买家下单', time: this.order.OMtime, active:true, next:true },
            { name:'买家支付', time: '已支付', active:true, next:true },
            { name:'商家发货', time: '待发货', active:false, next:false },
            { name:'交易完成', time: '未完成', active:false, next:false }]
          this.orderStatus = this.order.OMstatus
        }else if(this.order.OMstatus == '已发货') {
          this.step = [
            { name:'买家下单', time: this.order.OMtime, active:true, next:true },
            { name:'买家支付', time: '已支付', active:true, next:true },
            { name:'商家发货', time: '已发货', active:true, next:true },
            { name:'交易完成', time: '未完成', active:false, next:false }]
          this.orderStatus = this.order.OMstatus
        }else if(this.order.OMstatus == '已收货') {
          this.step = [
            { name:'买家下单', time: this.order.OMtime, active:true, next:true },
            { name:'买家支付', time: '已支付', active:true, next:true },
            { name:'买家收货', time: '已收货', active:true, next:true },
            { name:'交易完成', time: '未完成', active:false, next:false }]
          this.orderStatus = this.order.OMstatus
        }else if(this.order.OMstatus == '已完成') {
          this.step = [
            { name:'买家下单', time: this.order.OMtime, active:true, next:true },
            { name:'买家支付', time: '已支付', active:true, next:true },
            { name:'买家收货', time: '已收货', active:true, next:true },
            { name:'交易完成', time: '已完成', active:true, next:true }]
          this.orderStatus = this.order.OMstatus
        }else if(this.order.OMstatus == '已评价') {
          this.step = [
            { name:'买家下单', time: this.order.OMtime, active:true, next:true },
            { name:'买家支付', time: '已支付', active:true, next:true },
            { name:'交易完成', time: '已完成', active:true, next:true },
            { name:'填写评价', time: '已评价', active:true, next:true }]
          this.orderStatus = this.order.OMstatus
        }else if(this.order.OMstatus == '退款中') {
          this.step = [
            { name:'买家下单', time: this.order.OMtime, active:true, next:true },
            { name:'买家支付', time: '已支付', active:true, next:true },
            { name:'买家收货', time: '已收货', active:true, next:true },
            { name:'退款完成', time: '退款中', active:false, next:true }]
          this.orderStatus = this.order.OMstatus
        }
      }
    },
    created() {
      // this.order = this.$route.query.order;
      this.OMid = this.$route.query.OMid;
      this.getData(this.OMid)
      // console.log(this.OMid)
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
        width: 45%;
        float: left;
        .order-info-part {
          height: 1.8rem;
          .left-text-div {
            width: 20%;
            float: left;
          }
          .left-value-div {
            width: 80%;
            float: right;
          }
          .left-text {
            width: 90%;
            font-size: 14px;
            color: @greyColor;
            line-height: 0.12rem;
            margin: 0 0 0.15rem 0.2rem;
          }
        }
      }
      .details-middle-right {
        width: 53%;
        float: right;
        .m-step-part {
          .right-top-top {
            padding: 0.1rem;
            .left-icon {
              width: 10%;
              float: left;
              margin-left: 0.1rem;
              margin-top: 0.1rem;
            }
            .right-text {
              float: left;
              .right-top {
                font-size: 18px;
                font-weight:bold;
                margin-top: 0.17rem;
              }
            }
          }
          .right-middle {
            margin: 0.6rem 0.8rem 0 0.8rem;
            .where-list {
              margin: 0 0 0.1rem 0.3rem;
            }
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
              margin: -0.1rem 0.2rem 0.2rem 0.2rem;
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
          margin: 0 0.1rem 0.1rem 0;
        }
      }
    }
  }
</style>
