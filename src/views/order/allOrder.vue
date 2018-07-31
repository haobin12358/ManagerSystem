<template>
  <div class="all-order">
    <page-title :title="name" @freshClick="freshClick"></page-title>
    <div class="all-order-content">
      <div class="all-order-search">
        <div class="order-search-one">
          <div class="search-text-input">
            <div class="search-text" style="margin-left: 0.51rem">订单号：</div>
            <el-input v-model="OMidSearch" size="mini" placeholder="请输入订单号" clearable></el-input>
          </div>
          <div class="search-text-input">
            <div class="search-text">物流方式：</div>
            <el-select v-model="OMlogisticsNameSearch" placeholder="请选择" size="mini" clearable>
              <div v-for="item in OMlogisticsNameList">
                <el-option :label="item" :value="item"></el-option>
              </div>
            </el-select>
          </div>
        </div>
        <div class="order-search-two">
          <div class="search-text-input">
            <div class="search-text">商品名称：</div>
            <el-input v-model="PRnameSearch" size="mini" placeholder="请输入商品名称" clearable></el-input>
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
          <div v-for="item in tabList">
            <el-tab-pane :label="item" :name="item.slice(0, 3)" :lazy="lazyStatus">
              <all-order-table ref="child" :order="order" @toPage="getData"></all-order-table>
            </el-tab-pane>
          </div>
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
  import index from "../../router";
  export default {
    data() {
        return {
          name: '所有订单',
          activeName: '全 部',
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
          OMtime: null,
          OMlogisticsNameSearch: '',
          OMlogisticsNameList: [],
          lazyStatus: false,
          PRnameSearch: '',
          OMidSearch: '',
          orderList: [],
          search: {},
          order: {},
          page_size: 10,
          OMstatus: '',
          OMstartTime: '',
          OMendTime: '',
          tabList: ['全 部', '已取消','未支付','支付中', '已支付','已发货','已收货', '已完成','已评价','退款中'],
          index: 0
        }
    },
    components: { pageTitle, allOrderTable },
    methods: {
      // 页面刷新
      freshClick(){
        console.log('fresh');
      },
      // 获取点击tab的label
      handleClick(tab) {
        // 判断要调用哪个子组件的方法
        if(tab.index == 9) {
          this.index = 0
        }else {
          this.index = parseInt(tab.index) + 1
        }
        // 判断需要的订单状态
        if(tab.name == '全 部') {
          this.OMstatus = ''
        }else {
          this.OMstatus = tab.name
        }
        // this.tabList = ['全 部', '已取消','未支付','支付中', '已支付','已发货','已收货', '已完成','已评价','退款中']
        // tab.label含"0"则不调用接口
        if(tab.label.indexOf("0") == -1) {
          this.getData(1)
        }
      },
      // 获取订单数据
      getData(v){
        let params = {
          token: localStorage.getItem('token'),
          OMstatus: this.OMstatus,
          page_num: v,
          page_size: this.page_size,
          OMid: '',
          OMlogisticsName: '',
          PRname: '',
          OMstartTime: '',
          OMendTime: ''
        }
        if(this.search != '') {
            params.OMid =  this.search.OMid
            params.OMlogisticsName =  this.search.OMlogisticsName
            params.PRname =  this.search.PRname
            params.OMstartTime = this.search.OMstartTime
            params.OMendTime =  this.search.OMendTime
        }
        axios.get(api.get_all_order,{params:params}).then(res => {
          if(res.data.status == 200) {
            this.orderList = res.data.data.OrderMains;
            this.order = res.data.data
            // 仅在查询和点击“全部”Tab标签时，对tabList进行一次添加数量操作
            if(this.tabList[0].length == 3) {
              this.getTabs(this.order.OMcount)
            }
          }else{
            this.$message.error(res.data.message);
          }
        })
      },
      // 获取订单的各个状态及对应的数量，并添加到tabList中
      getTabs(OMcount) {
        let i = 0
        this.tabList[0] = this.tabList[0]+'('+this.orderList.length+')'
        for(let j=1;j<this.tabList.length;j++) {
          i = (j-1)*7
          this.tabList[j] = this.tabList[j]+'('+OMcount[i]+')'
        }
      },
      // 头部查询条件
      topSearch() {
        this.OMstatus = ''
        // 完善头部查询条件去除后获取数据的逻辑
        if(this.OMtime != null || this.PRnameSearch != '' || this.OMidSearch != '' || this.OMlogisticsNameSearch != '') {
          if(this.OMtime != null) {
            this.OMstartTime = this.OMtime[0]+' 00:00:00'
            this.OMendTime = this.OMtime[1]+' 23:59:59'
          }else if (this.OMtime == null) {
            this.OMstartTime = ''
            this.OMendTime = ''
          }
        }
        this.search = {
          OMid: this.OMidSearch,
          OMlogisticsName: this.OMlogisticsNameSearch,
          PRname: this.PRnameSearch,
          OMstartTime: this.OMstartTime,
          OMendTime: this.OMendTime
        }
        this.tabList = ['全 部', '已取消','未支付','支付中', '已支付','已发货','已收货', '已完成','已评价','退款中']
        this.getData(1)
      },
      getOMlogisticsNameList() {
        axios.get(api.get_omfilter).then(res => {
          if(res.data.status == 200) {
            for(let i=0;i<res.data.data.length;i++) {
              if(res.data.data[i].key == "OMlogisticsName") {
                this.OMlogisticsNameList = res.data.data[i].value
              }
            }
          }else{
            this.$message.error(res.data.message);
          }
        })
      }
    },
    created() {
      this.getData(1)
      this.getOMlogisticsNameList()
    },
    watch: {
      // 依据order变化来传递对应的新的order给对应的this.index的子组件，并调用该子组件的getOrderList方法
      order(newValue, oldValue) {
        this.$refs.child[this.index].getOrderList(newValue)
      }
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
