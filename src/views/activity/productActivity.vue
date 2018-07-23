<template>
  <div class="m-discount-index">
    <page-title :title="name" @freshClick="freshClick"></page-title>
    <div class="m-discount-content">
      <div class="m-discount-nav">
        <template v-for="(item,index) in tab_data" >
          <span class="m-one-nav" :class="item.show?'active':''"  @click="tabChange(item.url)">{{item.name}}</span>
        </template>
      </div>

      <!--店铺优惠券-->
      <div class="m-store" v-show="tab_data.activity.show">
        <el-form :inline="true" :model="storeForm" class="demo-form-inline">
          <div class="m-select-box">
            <div class="m-left">
              <el-form-item label="活动状态">
                <el-select v-model="storeForm.name" class="m-input-s" placeholder="活动区域">
                  <el-option label="区域一" value="shanghai"></el-option>
                  <el-option label="区域二" value="beijing"></el-option>
                </el-select>
              </el-form-item>
              <el-form-item label="活动名称">
                <el-input v-model="storeForm.name" class="m-input-s" placeholder="审批人"></el-input>
              </el-form-item>
              <el-form-item label="活动ID">
                <el-input v-model="storeForm.name" class="m-input-s" placeholder="审批人"></el-input>
              </el-form-item>
              <el-form-item>
                <el-button type="primary" class="m-select-btn" @click="storeSubmit">查询</el-button>
              </el-form-item>
            </div>
            <div class="m-right">
              <el-form-item>
                <el-button type="primary" class="m-select-btn" @click="addNew">创建</el-button>
              </el-form-item>
            </div>
          </div>
        </el-form>
        <div class="m-middle" style="width: 100%;margin-top: 0.1rem;">
          <el-table :data="user" stripe style="width: 100%">
            <el-table-column align="center" prop="userId" label="名称ID"></el-table-column>
            <el-table-column align="center" prop="userId" label="活动名称" ></el-table-column>
            <el-table-column align="center" prop="userName" label="活动描述"></el-table-column>
            <el-table-column align="center" prop="group" label="优惠类型" ></el-table-column>
            <el-table-column align="center" prop="group" label="活动时间" width="230">
              <template slot-scope="scope">
                <div class="m-activity-time">
                  <p><span>2018-07-02</span><span>20:20:13</span></p>
                  <p>至</p>
                  <p><span>2018-07-02</span><span>20:20:13</span></p>
                </div>
                <p>活动持续：12小时18分18秒</p>
              </template>
            </el-table-column>
            <el-table-column align="center" prop="group" label="创建时间" >
              <template slot-scope="scope">
                <p>2018-07-02</p>
                <p>20:20:13</p>
              </template>
            </el-table-column>
            <el-table-column align="center" prop="loginTime" label="活动状态" ></el-table-column>
            <el-table-column align="center" label="操作" width="160">
              <template slot-scope="scope">
                <span>查看</span>
                <span class="m-link">删除</span>
                <span class=" m-link">重启</span>
              </template>
            </el-table-column>
          </el-table>
        </div>
        <div class="m-page-box">
          <pagination></pagination>
        </div>
      </div>
      <!--dataInfo-->
      <div class="m-data-info" v-show="tab_data.dataInfo.show">
        <p class="m-date">
          <span>日</span>
          <el-date-picker
            v-model="value7"
            type="daterange"
            align="right"
            unlink-panels
            range-separator="至"
            start-placeholder="开始日期"
            end-placeholder="结束日期"
            :picker-options="pickerOptions2">
          </el-date-picker>
          <!--<span class="m-date-icon"></span>-->
        </p>
        <ul class="m-amount-sheet-ul">
          <template v-for="(item,index) in data_detail">
            <li class="m-amount-sheet" :class="item.click?'active':''" @click="numListClick(index)">
              <p>{{item.name}}</p>
              <p class="m-num">{{item.num}}</p>
              <p class="m-grey"><span>较前1日</span><span>↑</span></p>
            </li>
          </template>
        </ul>
        <div class="m-discount-echart">
          <div id="echarts"></div>
        </div>
      </div>
    </div>
  </div>

</template>
<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  import user from '../../common/json/userInfo';
  import Pagination from "../../components/common/pages";
  import echarts from 'echarts';
  export default {
    data() {
      return {
        name:'单品活动',
        storeForm:{
          name:'',
          date1:'',
          date2:''
        },
        tab_data:{
          activity:{
            name:'活动管理',
            url:'activity',
            show:true
          },
          dataInfo:{
            name:'数据概况',
            url:'dataInfo',
            show:false
          }
        },
        data_detail:[
          {
            name:'领取张数',
            num:20,
            down_up:'down',
            click:true
          }, {
            name:'使用张数',
            num:20,
            down_up:'down',
            click:false
          }, {
            name:'优惠金额',
            num:20,
            down_up:'down',
            click:false
          }, {
            name:'支付买家数',
            num:20,
            down_up:'down',
            click:false
          },
          {
            name:'支付件数',
            num:20,
            down_up:'down',
            click:false
          },
          {
            name:'交易金额',
            num:20,
            down_up:'down',
            click:false
          }
        ],
        user: user,
        option : {
          color:['#edb3b1'],
          tooltip:{
            show:true,
            position: 'top',
            padding: 10,
            backgroundColor:'#edb3b1',
            textStyle:{
              color: '#fff',
              fontSize:21
            }
          },
          xAxis: {
            type: 'category',
            data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            axisLine:{
              show:false
            }
          },
          yAxis: {
            type: 'value',
            axisLine:{
              show:false
            }
          },
          series: [{
            data: [820, 932, 901, 934, 1290, 1330, 1320],
            type: 'line'
          }]
        },
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
        value7: ''

      }
    },
    components:{
      pageTitle,
      Pagination
    },
    methods: {
      freshClick(){
        console.log('fresh');
      },
      storeSubmit(){

      },
      tabChange(v){
        this.tab_data[v].show = true;
        for(let item in this.tab_data){
          if(item != v){
            this.tab_data[item].show = false;
          }
        }
      },
      addNew(){
        this.$router.push('/activity/activityProductStepOne');
      },
      numListClick(v){
        for(let i = 0;i<this.data_detail.length;i++){
          this.data_detail[i].click = false;
        }
        this.data_detail[v].click = true;
      }
    },
    mounted(){
      let myChart = echarts.init(document.getElementById('echarts'));
      myChart.setOption(this.option);
    },
    created() {

    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/activity";

</style>
