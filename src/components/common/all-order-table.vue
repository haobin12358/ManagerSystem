<template>
  <div class="order-table">
    <el-table :data="orderList" style="width: 100%" class="out-table" :default-expand-all="expandAll" stripe size="mini">
      <el-table-column type="selection" width="30">
      </el-table-column>
      <el-table-column type="expand" width="30">
        <template slot-scope="scope">
          <el-table class="demo-table-expand" :data="scope.row.order_item" border style="width: 100%" stripe size="mini">
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
            <el-table-column align="center" prop="PBunit" label="价格单位">
            </el-table-column>
            <el-table-column align="center" prop="PRinfo" label="商品简介">
            </el-table-column>
            <el-table-column align="center" prop="PRtype" label="商品类型">
            </el-table-column>
            <el-table-column align="center" prop="PRbrand" label="商品分类">
            </el-table-column>
          </el-table>
        </template>
      </el-table-column>
      <el-table-column align="center" label="订单号" prop="OMid" width="350">
      </el-table-column>
      <el-table-column align="center" label="订单状态" prop="OMstatus" width="100">
      </el-table-column>
      <el-table-column align="center" label="订单价格" prop="OMprice" width="100">
      </el-table-column>
      <el-table-column align="center" label="下单时间" prop="OMtime" width="200">
      </el-table-column>
      <el-table-column align="center" label="订单备注" prop="OMabo">
      </el-table-column>
      <el-table-column align="center" label="操作" width="150">
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
  // 0: "已取消", 7: "未支付", 14: "支付中", 21: "已支付",28: "已发货", 35: "已收货", 42: "已完成", 49: "已评价", 56: "退款中"
  import Pagination from "../../components/common/page";
  import api from '../../api/api';
  import {Message} from 'element-ui';
  import axios from 'axios';
  export default {
    props: [],
    name: "all-order-table",
    data() {
      return {
        expandAll: false,
        orderList: [],
        total_page: 0,
        current_page: 0,
        total_num: 0,
        page_size: 10,
        OMstatus: ''
      }
    },
    components: {
      Pagination
    },
    methods: {
      orderDetails(order) {
        let OMid = order.OMid
        this.$router.push({path: '/order/orderDetails', query: {OMid}});
      },
      changeOMstatus(OMstatus) {
        if(OMstatus == '全部') {
          this.OMstatus = ''
        }else {
          this.OMstatus = OMstatus
        }
        this.getData(1)
        console.log('this.OMstatus', this.OMstatus)
      },
      getData(v){
        let params = {
          token: localStorage.getItem('token'),
          OMstatus: this.OMstatus,
          page_num: v,
          page_size: this.page_size
        };
        axios.get(api.get_all_order,{params:params}).then(res => {
          console.log('params.OMstatus', params.OMstatus)
          if(res.data.status == 200) {
            this.orderList = res.data.data.OrderMains;
            console.log(res.data.data)
            // console.log(this.orderList)
            this.total_num = res.data.data.count;
            this.total_page = Math.ceil(this.total_num / this.page_size);
          }else{
            this.$message.error(res.data.message);
          }
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
        console.log('page')
      },
    },
    created() {
      console.log('created')
      // this.orderList = allOrder;
      this.getData(1)
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
