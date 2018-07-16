<template>
  <div class="refund-table">
    <el-table :data="tableData" stripe style="width: 100%">
      <el-table-column prop="refundNo" label="退款编号">
      </el-table-column>
      <el-table-column prop="refundType" label="退款方式">
      </el-table-column>
      <el-table-column prop="orderNo" label="订单编号">
      </el-table-column>
      <el-table-column prop="good" label="商品">
      </el-table-column>
      <el-table-column prop="realPay" label="订单金额">
      </el-table-column>
      <el-table-column prop="refundAmount" label="退款金额">
      </el-table-column>
      <el-table-column prop="refundDate" label="退款时间">
      </el-table-column>
      <el-table-column prop="refundStatus" label="退款状态">
      </el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button @click="handleClick(scope.row)" type="text" class="operation-button">退款</el-button>
          <el-button type="text" class="operation-button" disabled>关闭</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
  import refundOrder from "../../common/json/refundOrder";
  export default {
    name: "refund-table",
    data() {
      return {
        tableData: []
      }
    },
    methods: {
      handleClick(row) {
        console.log(row)
      }
    },
    mounted() {
      this.tableData = refundOrder;
    }
  }
</script>


<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/_variate.less";
  .refund-table {
    .operation-button {
      color: @sidebarChildColor;
    }
  }
</style>
