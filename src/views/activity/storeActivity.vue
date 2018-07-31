<template>
  <div class="m-discount-index">
    <page-title :title="name" :fresh="true" @freshClick="freshClick"></page-title>
    <div class="m-discount-content">
      <div class="m-discount-top">
        <ul class="m-store-top">
          <li class="m-store-card" @click="storeCardClick">
            <div class="m-card-left">
              <span class="m-card-icon"></span>
            </div>
            <div class="m-card-right">
              <p class="m-title">+创建新活动</p>
              <p>自定义创建店铺活动</p>
            </div>
          </li>
          <!--<li class="m-store-card">-->
            <!--<div class="m-card-left">-->
              <!--<span>8</span>-->
            <!--</div>-->
            <!--<div class="m-card-right">-->
              <!--<p class="m-title">两件8折</p>-->
              <!--<p>任意两件商品8折</p>-->
            <!--</div>-->
          <!--</li>-->
          <!--<li class="m-store-card">-->
            <!--<div class="m-card-left">-->
              <!--<span>半</span>-->
            <!--</div>-->
            <!--<div class="m-card-right">-->
              <!--<p class="m-title">第二件半价</p>-->
              <!--<p>第二件商品半价</p>-->
            <!--</div>-->
          <!--</li>-->
        </ul>
      </div>
      <tabs :tab_data="tab_data" @tabChange="tabChange"></tabs>
      <!--店铺优惠券-->
      <div class="m-store" v-show="tab_data.activity.show">
        <el-form :inline="true" :model="storeForm" class="demo-form-inline">
          <div class="m-select-box">
            <div class="m-left">
              <el-form-item label="活动状态">
                <el-select v-model="storeForm.COstatus" class="m-input-s" placeholder="活动区域">
                  <el-option label="全部" value=""></el-option>
                  <el-option label="预热" value="预热"></el-option>
                  <el-option label="进行中" value="进行中"></el-option>
                  <el-option label="暂停" value="暂停"></el-option>
                  <el-option label="结束" value="介绍"></el-option>
                </el-select>
              </el-form-item>
              <el-form-item label="活动名称">
                <el-input v-model="storeForm.COname" class="m-input-s" placeholder=""></el-input>
              </el-form-item>
              <el-form-item label="活动编号">
                <el-input v-model="storeForm.COid" class="m-input-s" placeholder=""></el-input>
              </el-form-item>
              <el-form-item>
                <el-button type="primary" class="m-select-btn" @click="storeSubmit">查询</el-button>
              </el-form-item>
            </div>
          </div>
        </el-form>
        <div class="m-middle" style="width: 100%;margin-top: 0.1rem;">
          <el-table :data="activity_data" stripe style="width: 100%">
            <el-table-column align="center" prop="COid" label="名称编号"></el-table-column>
            <el-table-column align="center" prop="COname" label="活动名称" ></el-table-column>
            <el-table-column align="center" prop="COabo" label="活动详情"></el-table-column>
            <el-table-column align="center" prop="group" label="活动时间" width="200">
              <template slot-scope="scope">
                <div class="m-activity-time">
                  <p>{{scope.row.COstart}}</p>
                  <!--<p><span>2018-07-02</span><span>20:20:13</span></p>-->
                  <p>至</p>
                  <p>{{scope.row.COend}}</p>
                  <!--<p><span>2018-07-02</span><span>20:20:13</span></p>-->
                </div>
                <p>活动持续：1{{scope.row.duration}}</p>
              </template>
            </el-table-column>
            <el-table-column align="center" prop="COstatus" label="活动状态" ></el-table-column>
            <el-table-column align="center" label="操作" >
              <template slot-scope="scope">
                <span class="m-link m-first" @click="checkActivity(scope.row)">查看</span>
                <span class="m-link" @click="deleteActivity(scope.row)" >删除</span>
                <span class="m-link" @click="pauseActivity(scope.row)" >暂停</span>
                <span class=" m-link" @click="restartActivity(scope.row)" v-if="scope.row.COstatus == '暂停'">重启</span>
              </template>
            </el-table-column>
          </el-table>
        </div>
        <div class="m-page-box">
          <Pagination :total="page_data.total_page" @pageChange="pageChange"></Pagination>
        </div>
      </div>
      <!--dataInfo-->
      <div class="m-data-info" v-show="tab_data.dataInfo.show">
        <p class="m-date">
          <span>日</span>
          <el-date-picker
            v-model="situation_date"
            type="daterange"
            align="right"
            unlink-panels
            range-separator="至"
            start-placeholder="开始日期"
            end-placeholder="结束日期"
            :picker-options="pickerOptions2"
            value-format="yyyy-MM-dd HH:mm:ss"
          @change="dateChange">
          </el-date-picker>
          <!--<span class="m-date-icon"></span>-->
        </p>
        <num-list :num_data="data_detail" @numListClick="numListClick"></num-list>
        <m-echarts :width="1000" :height="300" :option="option" id="storeActivity"></m-echarts>
      </div>
    </div>
  </div>

</template>
<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  import Pagination from "../../components/common/page";
  import tabs from '../../components/common/tabs';
  import numList from '../../components/activity/numList';
  import mEcharts from '../../components/common/vue-echarts';
  import axios from 'axios';
  import api from '../../api/api';
  export default {
    data() {
      return {
        name:'店铺活动',
        storeForm:{
          COname:'',
          COid:'',
          COstatus:''
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
        activity_data:[],
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
        option_data: [],
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
        situation_date: '',
        page_data:{
          total_page:0,
          current_page:1,
          total_num:0,
          page_size:10
        }

      }
    },
    components:{
      pageTitle,
      Pagination,
      tabs,
      'num-list':numList,
      'm-echarts':mEcharts
    },
    mounted(){
      this.getData();
      this.getSituation();
    },
    methods: {
      /*获取表格数据*/
      getData(v,name,id,status){
        let params = {
          token:localStorage.getItem('token'),
          page_num: v || this.page_data.current_page,
          page_size:this.page_data.page_size,
          COname:name,
          COid:id,
          COstatus:status,
          COgenre:'活动'
        };
        axios.get(api.get_all_card,{params:params}).then(res => {
          if(res.data.status == 200) {
            this.activity_data = res.data.CouponsActives;
            this.page_data.total_num = res.data.count;
            this.page_data.total_page = Math.ceil(this.page_data.total_num / this.page_data.page_size);
          }else{
            this.$message.error(res.data.message);
          }
        },error => {
          this.$message.error(error.data.message);
        })
      },
      /*获取概况*/
      getSituation() {
        axios.get(api.get_situation,{params:{
          token:localStorage.getItem('token'),
            COgenre:'活动',
            start_time:this.situation_date[0] || '',
            end_time:this.situation_date[1] || ''
          }}).then(res => {
            if(res.data.status == 200){
              this.data_detail = res.data.data.params;
              this.option_data = res.data.data.data;
              this.dealOption(0);
              for(let i=0;i<this.data_detail.length;i++){
                this.data_detail[i].click = false
              }
              this.data_detail[0].click = true
            }else{
              this.$message.error(res.data.message);
            }
        },error => {
          this.$message.error(error.data.message);
        })
      },
      dealOption(v){
        let _xAxis = [];
        let _series = [];
        for(let key in this.option_data){
          _xAxis.push(key.slice(0,11));
          _series.push(this.option_data[key][v]);
        }
        this.option.xAxis.data = [].concat(_xAxis);
        this.option.series[0].data = [].concat(_series);
      },
      /*日期变化*/
      dateChange() {
        this.getSituation();
      },
      freshClick(){
        this.getData();
        this.getSituation();
      },
      /*搜索*/
      storeSubmit(){
        this.getData(1,this.storeForm.COname,this.storeForm.COid,this.storeForm.COstatus);
      },
      /*数据和店铺活动数tab切换*/
      tabChange(v){
        this.tab_data[v].show = true;
        for(let item in this.tab_data){
          if(item != v){
            this.tab_data[item].show = false;
          }
        }
      },
      /*添加新店铺活动*/
      storeCardClick(){
        this.$router.push('/activity/activityStoreStepOne');
      },
      /*张数点击切换*/
      numListClick(v){
        let  _arr = this.data_detail;
        for(let i = 0;i<_arr.length;i++){
          _arr[i].click = false;
        }
        _arr[v].click = true;
        this.data_detail = [].concat(_arr);
        this.dealOption(v)
      },
      /*查看*/
      checkActivity(v){
        this.$router.push('/activity/activityStoreStepOne?COid=' + v.COid);
      },
      /*删除*/
      deleteActivity(v){
        this.$confirm('确认将选中商品删除?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.changeStatus(v,'删除');
        }).catch(() => {
        });
      },
      /*暂停*/
      pauseActivity(v){
        this.$confirm('确认将选中商品暂停吗 ?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.changeStatus(v,'暂停');
        }).catch(() => {
        });

      },
      /*重启*/
      restartActivity(v){
        this.$confirm('确认将选中商品重启吗 ?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.changeStatus(v,'进行中');
        }).catch(() => {
        });

      },
      changeStatus(v,status){
        axios.post(api.update_active_status+'?token=' +localStorage.getItem('token') ,{
          COid:v.COid,
          COstatus:status
        }).then(res => {
          if(res.data.status == 200){
            this.$message({
              message: '更新成功',
              type: 'success'
            });
            this.getData()
          }else{
            this.$message.error(res.data.message);
          }
        },error => {
          this.$message.error(error.data.message);
        })
      },
      /*分页点击*/
      pageChange(v){
        if(v == this.page_data.current_page){
          this.$message({
            message: '这已经是第' + v + '页数据了',
            type: 'warning'
          });
          return false;
        }
        this.page_data.current_page = v;
        this.getData(v);
      }
    },
    created() {

    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/activity";

</style>
