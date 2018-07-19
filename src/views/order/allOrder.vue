<template>
  <div class="all-order">
    <page-title :title="name" @freshClick="freshClick"></page-title>
    <div class="all-order-content">
      <div class="all-order-search">
        <div class="order-search-one">
          <div class="search-text-input">
            <div class="search-text" style="margin-left: 0.51rem">订单号：</div>
            <el-input size="mini"></el-input>
          </div>
          <div class="search-text-input">
            <div class="search-text">维权状态：</div>
            <el-select v-model="value" placeholder="请选择" size="mini">
              <el-option label="中通快递" value="中通快递"></el-option>
              <el-option label="中通快递" value="中通快递"></el-option>
              <el-option label="中通快递" value="中通快递"></el-option>
            </el-select>
          </div>
          <div class="search-text-input">
            <div class="search-text">付款方式：</div>
            <el-select v-model="value" placeholder="请选择" size="mini">
              <el-option label="中通快递" value="中通快递"></el-option>
              <el-option label="中通快递" value="中通快递"></el-option>
              <el-option label="中通快递" value="中通快递"></el-option>
            </el-select>
          </div>
        </div>
        <div class="order-search-two">
          <div class="search-text-input">
            <div class="search-text">商品名称：</div>
            <el-input size="mini"></el-input>
          </div>
          <div class="search-text-input">
            <div class="search-text">物流方式：</div>
            <el-select v-model="value" placeholder="请选择" size="mini">
              <el-option label="中通快递" value="中通快递"></el-option>
              <el-option label="中通快递" value="中通快递"></el-option>
              <el-option label="中通快递" value="中通快递"></el-option>
            </el-select>
          </div>
          <div class="search-text-input">
            <div class="search-text">订单类型：</div>
            <el-select v-model="value" placeholder="请选择" size="mini">
              <el-option label="中通快递" value="中通快递"></el-option>
              <el-option label="中通快递" value="中通快递"></el-option>
              <el-option label="中通快递" value="中通快递"></el-option>
            </el-select>
          </div>
        </div>
        <div class="order-search-three">
          <div class="search-text-input" style="width: 5rem">
            <div class="search-text">退款时间：</div>
            <div class="block">
              <el-date-picker v-model="value7" type="daterange" align="right" unlink-panels range-separator="至" start-placeholder="开始日期" end-placeholder="结束日期"
                              :picker-options="pickerOptions2" size="mini">
              </el-date-picker>
            </div>
          </div>
        </div>
        <div class="search-buttons">
          <el-button class="search-button" size="mini">筛选</el-button>
          <el-button class="search-button" size="mini">批量导出</el-button>
        </div>
      </div>
      <div class="all-order-tabs">
        <el-tabs v-model="activeName" @tab-click="handleClick">
          <el-tab-pane label="全部" name="one">
            <all-order-table></all-order-table>
          </el-tab-pane>
          <el-tab-pane label="待付款" name="two">待付款</el-tab-pane>
          <el-tab-pane label="待发货" name="three">待发货</el-tab-pane>
          <el-tab-pane label="已发货" name="four">已发货</el-tab-pane>
          <el-tab-pane label="已完成" name="five">已完成</el-tab-pane>
          <el-tab-pane label="已关闭" name="six">已关闭</el-tab-pane>
          <el-tab-pane label="退款中" name="seven">退款中</el-tab-pane>
        </el-tabs>
      </div>
    </div>
  </div>
</template>
<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  import allOrderTable from '../../components/common/all-order-table';
  export default {
      data() {
          return {
            name: '所有订单',
            activeName: 'one',
            pickerOptions2: {
              shortcuts: [{
                text: '最近一周',
                onClick(picker) {
                  const end = new Date();
                  const start = new Date();
                  start.setTime(start.getTime() - 3600 * 1000 * 24 * 7);
                  picker.$emit('pick', [start, end]);
                }
              }, {
                text: '最近一个月',
                onClick(picker) {
                  const end = new Date();
                  const start = new Date();
                  start.setTime(start.getTime() - 3600 * 1000 * 24 * 30);
                  picker.$emit('pick', [start, end]);
                }
              }, {
                text: '最近三个月',
                onClick(picker) {
                  const end = new Date();
                  const start = new Date();
                  start.setTime(start.getTime() - 3600 * 1000 * 24 * 90);
                  picker.$emit('pick', [start, end]);
                }
              }]
            },
            value7: '',
            value: ''
          }
      },
      components: {
        'pageTitle': pageTitle,
        'allOrderTable': allOrderTable
      },
      methods: {
        freshClick(){
          console.log('fresh');
        },
        handleClick(tab, event) {
          // console.log(tab, event);
        }
      },
      created() {

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
        height: 1rem;
        padding: 0.2rem 0.3rem 0 0.3rem;
        margin: 0.15rem 0.2rem 0 0.2rem;
        border-radius: 0.1rem;
        background-color: @borderColor;
        .search-buttons {
          float: right;
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
