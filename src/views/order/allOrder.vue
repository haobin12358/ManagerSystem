<template>
  <div class="all-order">
    <page-title :title="name" @freshClick="freshClick"></page-title>
    <div class="all-order-content">
      <div class="all-order-search">
        <div class="order-search-one">
          <div class="search-text-input">
            <div class="search-text">商品名称：</div>
            <el-input v-model="PRnameSearch" size="mini" placeholder="请输入商品名称" clearable></el-input>
          </div>
          <!--<div class="search-text-input">
            <div class="search-text">订单状态：</div>
            <el-select v-model="value" placeholder="请选择" size="mini">
              <el-option label="中通快递" value="中通快递"></el-option>
              <el-option label="中通快递" value="中通快递"></el-option>
              <el-option label="中通快递" value="中通快递"></el-option>
            </el-select>
          </div>-->
        </div>
        <div class="order-search-two">
          <div class="search-text-input">
            <div class="search-text" style="margin-left: 0.51rem">订单号：</div>
            <el-input v-model="OMidSearch" size="mini" placeholder="请输入订单号" clearable></el-input>
          </div>
          <div class="search-text-input" style="width: 5rem">
            <div class="search-text">下单时间：</div>
            <div class="block">
              <el-date-picker v-model="OMtime" type="daterange" unlink-panels range-separator="至" start-placeholder="开始日期" end-placeholder="结束日期"
                              :picker-options="pickerOptions2" size="mini" value-format="yyyy-MM-dd">
              </el-date-picker>
            </div>
          </div>
        </div>
        <div class="search-buttons">
          <el-button class="search-button" size="mini" @click="topSearch">查询</el-button>
          <el-button class="search-button" size="mini">批量导出</el-button>
        </div>
      </div>
      <div class="all-order-tabs">
        <el-tabs v-model="activeName" @tab-click="handleClick">
          <el-tab-pane label="全部（7）" name="全部" :lazy="lazyStatus">
            <all-order-table ref="child" @toPage="getData"></all-order-table>
          </el-tab-pane>
          <el-tab-pane label="已取消（7）" name="已取消" :lazy="lazyStatus">
            <all-order-table ref="child" @toPage="getData"></all-order-table>
          </el-tab-pane>
          <el-tab-pane label="未支付（7）" name="未支付" :lazy="lazyStatus">
            <all-order-table ref="child" @toPage="getData"></all-order-table>
          </el-tab-pane>
          <el-tab-pane label="支付中（7）" name="支付中" :lazy="lazyStatus">
            <all-order-table ref="child" @toPage="getData"></all-order-table>
          </el-tab-pane>
          <el-tab-pane label="已支付（7）" name="已支付" :lazy="lazyStatus">
            <all-order-table ref="child" @toPage="getData"></all-order-table>
          </el-tab-pane>
          <el-tab-pane label="已发货（7）" name="已发货" :lazy="lazyStatus">
            <all-order-table ref="child" @toPage="getData"></all-order-table>
          </el-tab-pane>
          <el-tab-pane label="已收货（7）" name="已收货" :lazy="lazyStatus">
            <all-order-table ref="child" @toPage="getData"></all-order-table>
          </el-tab-pane>
          <el-tab-pane label="已完成（7）" name="已完成" :lazy="lazyStatus">
            <all-order-table ref="child" @toPage="getData"></all-order-table>
          </el-tab-pane>
          <el-tab-pane label="已评价（7）" name="已评价" :lazy="lazyStatus">
            <all-order-table ref="child" @toPage="getData"></all-order-table>
          </el-tab-pane>
          <el-tab-pane label="退款中（7）" name="退款中" :lazy="lazyStatus">
            <all-order-table ref="child" @toPage="getData"></all-order-table>
          </el-tab-pane>
        </el-tabs>
      </div>
    </div>
  </div>
</template>
<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  import allOrderTable from '../../components/common/all-order-table';
  import api from '../../api/api';
  import {Message} from 'element-ui';
  import axios from 'axios';
  export default {
      data() {
          return {
            name: '所有订单',
            activeName: '全部',
            pickerOptions2: {
              shortcuts: [
                {
                  text: '最近一周',
                  onClick(picker) {
                    const end = new Date();
                    const start = new Date();
                    start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
                    picker.$emit('pick', [start, end]);
                  }
                },
                {
                  text: '最近一个月',
                  onClick(picker) {
                    const end = new Date();
                    const start = new Date();
                    start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
                    picker.$emit('pick', [start, end]);
                  }
                },
                {
                  text: '最近三个月',
                  onClick(picker) {
                    const end = new Date();
                    const start = new Date();
                    start.setTime(start.getTime() - 3600 * 1000 * 24 * 90);
                    picker.$emit('pick', [start, end]);
                  }
                }
              ]
            },
            OMtime: '',
            // value: '',
            lazyStatus: true,
            PRnameSearch: '',
            OMidSearch: '',
            orderList: [],
            page_size: 10,
            OMstatus: '',
            OMstartTime: '',
            OMendTime: '',
            tabList: ['全部', '已取消','未支付','支付中', '已支付','已发货','已收货', '已完成','已评价','退款中']
          }
      },
      components: {
        'pageTitle': pageTitle,
        'allOrderTable': allOrderTable
      },
      methods: {
        // 页面刷新
        freshClick(){
          console.log('fresh');
        },
        // 获取点击tab的label
        handleClick(tab) {
          this.changeOMstatus(tab.name)
        },
        // 判断需要的订单状态
        changeOMstatus(OMstatus) {
          if(OMstatus == '全部') {
            this.OMstatus = ''
          }else {
            this.OMstatus = OMstatus
          }
          this.getData(1)
        },
        // 获取订单数据
        getData(v){
          let params = {
            token: localStorage.getItem('token'),
            OMstatus: this.OMstatus,
            page_num: v,
            page_size: this.page_size,
            PRname: this.PRnameSearch,
            OMstartTime: this.OMstartTime,
            OMendTime: this.OMendTime,
            OMid: this.OMidSearch
          }
          axios.get(api.get_all_order,{params:params}).then(res => {
            if(res.data.status == 200) {
              this.orderList = res.data.data.OrderMains;
              this.getTabs(res.data.data.OMcount);
              this.$refs.child.getOrderList(res.data.data, this.page_size)
            }else{
              this.$message.error(res.data.message);
            }
          })
        },
        // 获取订单的各个状态及对应的数量
        getTabs(OMcount) {
          let i = 0
          this.tabList[0] = this.tabList[0]+'( '+this.orderList.length+' )'
          for(let j=1;j<this.tabList.length;j++) {
            i = (j-1)*7
            this.tabList[j] = this.tabList[j]+'( '+OMcount[i]+' )'
          }
        },
        // 头部查询条件
        topSearch() {
          this.OMstartTime = this.OMtime[0]+' 00:00:00'
          this.OMendTime = this.OMtime[1]+' 23:59:59'
          this.getData(1)
        }
      },
      created() {
        this.getData(1)
      }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/_variate.less";
  .all-order {
    background-color: @bgMainColor;
    .all-order-content {
      background-color: @bgMainColor;
      .all-order-search {
        height: 0.75rem;
        padding: 0.2rem 0.3rem 0 0.3rem;
        margin: 0.15rem 0.2rem 0 0.2rem;
        border-radius: 0.1rem;
        background-color: @borderColor;
        .search-buttons {
          float: right;
          /*margin-top: -0.3rem;*/
          margin-right: 1.15rem;
          .search-button {
            background-color: @btnActiveColor;
            color: @bgMainColor;
            font-size: 14px;
          }
          .el-button:active {
            color: @sectionBgColor;
            border-color: @sectionBgColor;
            outline: 0;
          }
        }
      }
      .all-order-tabs {
        width: 100%;
        background-color: @bgMainColor;
        .el-tabs {
          padding: 0.2rem;
        }
      }
    }
  }
  .search-text-input {
    float: left;
    width: 3.2rem;
    margin-bottom: 0.1rem;
    .search-text {
      float: left;
      margin-left: 0.4rem;
      line-height: 0.22rem;
      font-size: 14px;
    }
    .search-text-middle {
      float: left;
      font-size: 14px;
      line-height: 0.22rem;
      margin: 0 0.1rem 0 0.1rem;
    }
    .el-input {
      float: left;
      width: 1.6rem;
    }
  }
</style>
