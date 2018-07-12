<template>
  <div class="order-table">
    <div class="order-table-header">
      <el-table :data="tableData" stripe style="width: 100%">
        <el-table-column prop="date" label="商品"></el-table-column>
        <el-table-column prop="date" label="单价/数量"></el-table-column>
        <el-table-column prop="date" label="售后"></el-table-column>
        <el-table-column prop="date" label="买家"></el-table-column>
        <el-table-column prop="date" label="下单时间"></el-table-column>
        <el-table-column prop="date" label="订单状态"></el-table-column>
        <el-table-column prop="date" label="实付金额"></el-table-column>
      </el-table>
    </div>
  </div>
</template>

<script>
  export default {
    props: [],
    name: "all-order-table",
    data() {
      return {

      }
    },
    components: {

    }
  }
</script>

<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/_variate.less";
  .order-table {
    .order-table-header {
      .el-table {
        .el-table-column {
          text-align: center;
        }
      }
    }
  }

</style>
