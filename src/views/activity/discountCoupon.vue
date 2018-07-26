<template>
  <div class="m-discount-index">
    <page-title :title="name" @freshClick="freshClick"></page-title>
    <div class="m-discount-content">
        <div class="m-discount-top">
          <div class="m-discount-top-part">
            <div class="m-top-img"></div>
            <div class="m-top-info">
              <p>优惠券</p>
              <p class="m-info-grey">可通过多种渠道推广的电子券，通过设置优惠金额和使用门槛，刺激转化提高客单，</p>
              <p class="m-info-grey">包括店铺优惠券和商品优惠券。</p>
              <p>店铺优惠券：可创建 <span class="m-num">20</span> 个 &nbsp;&nbsp; 店铺优惠券：可创建 <span class="m-num">20</span> 个</p>
            </div>
          </div>
          <div class="m-discount-top-part">
            <router-link to="/activity/discountStoreStepOne" >
              <div class="m-top-btn">+店铺优惠券</div>
            </router-link>
            <router-link to="/activity/discountProductStepOne" >
              <div class="m-top-btn">+商品优惠券</div>
            </router-link>

          </div>
        </div>
      <tabs :tab_data="tab_data" @tabChange="tabChange"></tabs>
      <!--数据详情-->
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
        <num-list :num_data="data_detail" @numListClick="numListClick"></num-list>
        <m-echarts :width="1000" :height="300" :option="option" :id="id"></m-echarts>
      </div>

      <!--店铺优惠券-->
      <div class="m-store" v-show="tab_data.store.show">
          <el-form :inline="true" :model="storeForm" class="demo-form-inline">
            <div class="m-select-box">
              <div class="m-left">
                <el-form-item label="活动状态">
                  <el-select v-model="storeForm.name" class="m-input-s" placeholder="活动区域">
                    <el-option label="区域一" value="shanghai"></el-option>
                    <el-option label="区域二" value="beijing"></el-option>
                  </el-select>
                </el-form-item>
                <el-form-item label="优惠券名称">
                  <el-input v-model="storeForm.name" class="m-input-s" placeholder="审批人"></el-input>
                </el-form-item>
                <el-form-item label="面额">
                  <el-input v-model="storeForm.name" class="m-input-s" placeholder="审批人"></el-input>
                </el-form-item>
                <el-form-item label="时间">
                  <el-date-picker type="date" class="m-input-s" placeholder="起始时间" v-model="storeForm.date1" style="width: 1.2rem;"></el-date-picker>
                </el-form-item>
                <el-form-item label="-">
                  <el-date-picker type="date" class="m-input-s" placeholder="结束时间" v-model="storeForm.date2" style="width: 1.2rem;"></el-date-picker>
                </el-form-item>
              </div>
              <div class="m-right">
                <el-form-item>
                  <el-button type="primary" class="m-select-btn" @click="storeSubmit">查询</el-button>
                </el-form-item>
              </div>
            </div>
          </el-form>
        <div class="m-middle" style="width: 100%;margin-top: 0.1rem;">
          <el-table :data="user" stripe style="width: 100%">
            <el-table-column align="center" prop="userId" label="名称/渠道"></el-table-column>
            <el-table-column align="center" prop="userId" label="状态" ></el-table-column>
            <el-table-column align="center" prop="userName" label="面额"></el-table-column>
            <el-table-column align="center" prop="group" label="门槛" ></el-table-column>
            <el-table-column align="center" prop="group" label="使用时间" >
              <template slot-scope="scope">
               <p>起：2018-07-02</p>
                <p>止：2018-07-08</p>
              </template>
            </el-table-column>
            <el-table-column align="center" prop="group" label="限额" ></el-table-column>
            <el-table-column align="center" prop="loginTime" label="发行量" ></el-table-column>
            <el-table-column align="center" prop="group" label="已领取" ></el-table-column>
            <el-table-column align="center" label="操作" >
              <template slot-scope="scope">
                <span class="m-link m-first" @click="storeEdit">编辑</span>
              </template>
            </el-table-column>
          </el-table>
        </div>
        <div class="m-page-box">
          <pagination></pagination>
        </div>
      </div>
      <!--商品优惠卷-->
      <div class="m-commodity" v-show="tab_data.commodity.show">
        <el-form :inline="true" :model="storeForm" class="demo-form-inline">
          <div class="m-select-box">
            <div class="m-left">
              <el-form-item label="活动状态">
                <el-select v-model="storeForm.name" class="m-input-s" placeholder="活动区域">
                  <el-option label="区域一" value="shanghai"></el-option>
                  <el-option label="区域二" value="beijing"></el-option>
                </el-select>
              </el-form-item>
              <el-form-item label="优惠券名称">
                <el-input v-model="storeForm.name" class="m-input-s" placeholder="审批人"></el-input>
              </el-form-item>
              <el-form-item label="面额">
                <el-input v-model="storeForm.name" class="m-input-s" placeholder="审批人"></el-input>
              </el-form-item>
              <el-form-item label="时间">
                <el-date-picker type="date" class="m-input-s" placeholder="起始时间" v-model="storeForm.date1" style="width: 1.2rem;"></el-date-picker>
              </el-form-item>
              <el-form-item label="-">
                <el-date-picker type="date" class="m-input-s" placeholder="结束时间" v-model="storeForm.date2" style="width: 1.2rem;"></el-date-picker>
              </el-form-item>
            </div>
            <div class="m-right">
              <el-form-item>
                <el-button type="primary" class="m-select-btn" @click="storeSubmit">查询</el-button>
              </el-form-item>
            </div>
          </div>
        </el-form>
        <div class="m-middle" style="width: 100%;margin-top: 0.1rem;">
          <el-table :data="user" stripe style="width: 100%">
            <el-table-column align="center" prop="userId" label="名称/渠道"></el-table-column>
            <el-table-column align="center" prop="userId" label="状态" ></el-table-column>
            <el-table-column align="center" prop="userName" label="面额"></el-table-column>
            <el-table-column align="center" prop="group" label="门槛" ></el-table-column>
            <el-table-column align="center" prop="group" label="使用时间" >
              <template slot-scope="scope">
                <p>起：2018-07-02</p>
                <p>止：2018-07-08</p>
              </template>
            </el-table-column>
            <el-table-column align="center" prop="group" label="限额" ></el-table-column>
            <el-table-column align="center" prop="loginTime" label="发行量" ></el-table-column>
            <el-table-column align="center" prop="group" label="已领取" ></el-table-column>
            <el-table-column align="center" label="操作" >
              <template slot-scope="scope">
                <span class="m-link m-first" @click="storeEdit">编辑</span>
              </template>
            </el-table-column>
          </el-table>
        </div>
        <div class="m-page-box">
          <pagination></pagination>
        </div>
      </div>
    </div>
  </div>

</template>
<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  import echarts from 'echarts';
  import user from '../../common/json/userInfo';
  import Pagination from "../../components/common/pages";
  import tabs from '../../components/common/tabs';
  import numList from '../../components/activity/numList';
  import mEcharts from '../../components/common/vue-echarts';
  export default {
    data() {
      return {
        id:'discountCoupon',
        name:'优惠券',
        storeForm:{
          name:'',
          date1:'',
          date2:''
        },
        tab_data:{
          dataInfo:{
            name:'数据概况',
            url:'dataInfo',
            show:true
          },
          store:{
            name:'店铺优惠劵',
            url:'store',
            show:false
          },
          commodity:{
            name:'商品优惠券',
            url:'commodity',
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
      Pagination,
      tabs,
      'num-list':numList,
      'm-echarts':mEcharts
    },
    methods: {
      /*刷新*/
      freshClick(){
        console.log('fresh');
      },
      /*搜索*/
      storeSubmit(){

      },
      /*数据概况/店铺优惠券的切换*/
      tabChange(v){
        this.tab_data[v].show = true;
       for(let item in this.tab_data){
         if(item != v){
          this.tab_data[item].show = false;
         }
       }
      },
      /*+店铺优惠券*/
      storeEdit(){
        this.$router.push('/activity/discountStoreStepOne');
      },
      /*张数点击，数据切换*/
      numListClick(v){
        for(let i = 0;i<this.data_detail.length;i++){
          this.data_detail[i].click = false;
        }
        this.data_detail[v].click = true;
      }
    },
    mounted(){
    },
    created() {

    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/index";
  @import "../../common/css/activity";




</style>
