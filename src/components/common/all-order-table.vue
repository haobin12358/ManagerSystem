<template>
  <div class="order-table">
    <el-table :data="orderList" style="width: 100%" class="out-table" size="mini">
      <el-table-column type="selection" width="30">
      </el-table-column>
      <el-table-column type="expand" width="30">
        <template slot-scope="scope">
          <el-table class="demo-table-expand" :data="scope.row.goods" border style="width: 100%" stripe size="mini">
            <el-table-column align="center" prop="goodsName" label="商品">
            </el-table-column>
            <el-table-column align="center" prop="goodsPrice" label="单价">
            </el-table-column>
            <el-table-column align="center" prop="goodsNumber" label="数量">
            </el-table-column>
            <el-table-column align="center" prop="afterSales" label="售后">
            </el-table-column>
            <el-table-column align="center" prop="buyer" label="买家">
            </el-table-column>
            <el-table-column align="center" prop="orderTime" label="下单时间">
            </el-table-column>
            <el-table-column align="center" prop="status" label="订单状态">
            </el-table-column>
            <el-table-column align="center" prop="realPay" label="实付金额">
            </el-table-column>
          </el-table>
        </template>
      </el-table-column>
      <el-table-column align="center" label="订单号" prop="orderNo">
      </el-table-column>
      <el-table-column align="center" label="支付方式" prop="payType">
      </el-table-column>
      <el-table-column align="center" label="外部订单号" prop="outOrderNo">
      </el-table-column>
      <el-table-column align="center" label="支付流水号" prop="payNo">
      </el-table-column>
      <el-table-column align="center" label="操作">
        <template slot-scope="scope">
          <el-button size="mini" class="order-details" @click="orderDetails(scope.row)">订单详情
          </el-button>
        </template>
      </el-table-column>
    </el-table>
    <div class="page-button">
      <Pagination :total="total_page" @pageChange="pageChange"></Pagination>
    </div>
  </div>
</template>

<script>
  // 1、待付款，2、待发货，3、已发货，4、已完成，5、已关闭，6、退款中
  import allOrder from "../../common/json/allOrder";
  import Pagination from "../../components/common/page";
  import api from '../../api/api';
  import {Message} from 'element-ui';
  import axios from 'axios';
  export default {
    props: [],
    name: "all-order-table",
    data() {
      return {
        orderList: [],
        total_page:1,
        current_page:1,
        total_num:0,
        page_size:10
      }
    },
    components: {
      Pagination
    },
    methods: {
      orderDetails(order) {
        this.$router.push({path: '/order/orderDetails', query: {order}});
      },
      getData(v){
        let params = {
          token:localStorage.getItem('token'),
          OMstatus:'7'
        };
        axios.get(api.get_all_order,{params:params}).then(res => {
          console.log(res.data.data)
          if(res.data.status == 200) {
            // this.orderList = res.data.data;
            this.total_num = res.data.data.count;
            this.total_page = Math.ceil(this.total_num / this.page_size);
          }else{
            this.$message.error(res.data.message);
          }
        },error => {
          this.$message.error(error.data.message);
        })
      },
      pageChange(v){
        if(v == this.current_page){
          this.$message({
            message: '这已经是第' + v + '页数据了',
            type: 'warning'
          });
          return false;
        }
        this.current_page = v;
        this.getData(v);
      }
    },
    mounted() {
      this.orderList = allOrder;
      this.pageChange(2)
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/_variate.less";
  .order-table {
    .out-table {
      font-size: 14px;
    }
    .page-button {
      margin-top: 0.3rem;
    }
    .order-details {
      background-color: @btnActiveColor;
      color: @bgMainColor;
      font-size: 14px;
    }
  }

</style>
