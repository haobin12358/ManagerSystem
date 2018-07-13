<template>
  <div class="order-table">
    <div class="order-table-header">
      <el-table :data="tableData5" style="width: 100%" default-expand-all size="mini">
        <el-table-column type="selection" width="30">
        </el-table-column>
        <el-table-column type="expand" width="30">
          <template slot-scope="scope">
            <el-table class="demo-table-expand" :data="scope.row.goods" border style="width: 100%" :show-header="false" stripe size="mini">
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
              <el-table-column align="center" label="操作">
              </el-table-column>
            </el-table>
          </template>
        </el-table-column>
        <el-table-column align="right" label="商品" prop="orderNoText">
        </el-table-column>
        <el-table-column align="left" label="单价" prop="orderNo">
        </el-table-column>
        <el-table-column align="right" label="数量" prop="payTypeText">
        </el-table-column>
        <el-table-column align="left" label="售后" prop="payType">
        </el-table-column>
        <el-table-column align="right" label="买家" prop="outOrderNoText">
        </el-table-column>
        <el-table-column align="left" label="下单时间" prop="outOrderNo">
        </el-table-column>
        <el-table-column align="right" label="订单状态" prop="payNoText">
        </el-table-column>
        <el-table-column align="left" label="实付金额" prop="payNo">
        </el-table-column>
        <el-table-column align="center" label="操作">
          <template slot-scope="scope">
            <el-button size="mini" class="order-details" @click="orderDetails(scope.row)">订单详情
            </el-button>
          </template>
        </el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
  // 1、待付款，2、待发货，3、已发货，4、已完成，5、已关闭，6、退款中
  import allOrder from "../../common/json/allOrder";
  export default {
    props: [],
    name: "all-order-table",
    data() {
      return {
        tableData5: [],
      }
    },
    components: {

    },
    methods: {
      orderDetails(order) {
        this.$router.push({path: '/order/orderDetails', query: {order}});
        // console.log(order);
      }
    },
    mounted() {
      this.tableData5 = allOrder;
    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/_variate.less";
  .order-table {
    .order-details {
      background-color: @btnActiveColor;
      color: @bgMainColor;
      font-size: 14px;
    }
  }

</style>
