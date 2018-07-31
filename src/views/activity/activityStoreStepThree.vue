<template>
  <div class="m-step">
    <page-title :list="title_list" @freshClick="freshClick"></page-title>
    <el-form  :model=" $store.state.activity" ref="storeForm" :rules="rules" label-width="1.2rem" class="demo-ruleForm" :disabled="$store.state.activity.disabled">
      <div class="m-step-content">
        <h3 class="m-step-title">创建新活动</h3>
        <div class="m-step-part">
          <step :list="step"></step>
        </div>
        <div class="m-step-part">
          <h3 class="m-step-h3 m-flex-between">
            <span>活动名称：{{$store.state.activity.COname}}</span>
          </h3>
          <div>
            <table class="m-activity-table" width="100%">
              <tr>
                <td width="250">活动描述：<span>{{$store.state.activity.COabo}}</span></td>
                <td>活动时间：<span>{{$store.state.activity.COstart}} 至 {{$store.state.activity.COend}}</span></td>
                <td width="320">活动预热：<span>预热</span></td>
              </tr>
              <tr>
                <td>活动类型：<span>{{$store.state.activity.COtype}}</span></td>
                <!--<td>创建时间：<span>2018-06-29  00 : 00：01 </span></td>-->
              </tr>
            </table>
          </div>
        </div>
        <el-form-item label="优惠类型：" prop="ACbrand">
          <p>
            <el-radio v-model="$store.state.activity.COproduct" label="自选商品">自选商品</el-radio>
          </p>
          <p>
            <el-radio v-model="$store.state.activity.COproduct" label="全店商品">全店商品</el-radio>
          </p>
        </el-form-item>
        <el-form :inline="true" :model="storeForm" class="demo-form-inline" v-if=" $store.state.activity.COproduct == '自选商品'">
          <div class="m-select-box">
            <div class="m-left">
              <el-form-item label="商品名称">
                <el-input v-model="storeForm.name" class="m-input-s" placeholder=""></el-input>
              </el-form-item>
              <el-form-item label="商品状态">
                <el-select v-model="storeForm.status" class="m-input-s" placeholder="">
                  <el-option label="全部" value=""></el-option>
                  <el-option label="上架状态" value="上架状态"></el-option>
                  <el-option label="下架状态" value="下架状态"></el-option>
                  <el-option label="预售中" value="预售中"></el-option>
                </el-select>
              </el-form-item>
            </div>
            <div class="m-right">
              <el-form-item>
                <el-button type="primary" class="m-select-btn" @click="onSubmit">搜索</el-button>
              </el-form-item>
            </div>
          </div>
        </el-form>
        <div class="m-middle" style="width: 100%;margin-top: 0.1rem;" v-if=" $store.state.activity.COproduct == '自选商品'">
          <el-table :data="product_data" stripe style="width: 100%" ref="table" @selection-change="changeFun">
            <el-table-column type="selection" width="55"></el-table-column>
            <el-table-column align="center" prop="userId" width="400" label="宝贝描述">
              <template slot-scope="scope">
                <div class="m-production-description">
                  <img class="m-img" :src="scope.row.PRimage[0]" style="width: 0.6rem;height:0.6rem;" />
                  <div>
                    <p>{{scope.row.PRname}}</p>
                    <p>{{scope.row.PRid}}</p>
                  </div>
                </div>
              </template>
            </el-table-column>
            <el-table-column align="center" prop="userId" label="价格" ></el-table-column>
            <el-table-column align="center" prop="PRstatus" label="状态" ></el-table-column>
            <el-table-column align="center" prop="PRstock" label="库存" ></el-table-column>
            <!--<el-table-column align="center" label="操作" >-->
              <!--<template slot-scope="scope">-->
                <!--<span class="m-link m-first">参加活动</span>-->
              <!--</template>-->
            <!--</el-table-column>-->
          </el-table>
        </div>
        <div class="m-page-box" v-if=" $store.state.activity.COproduct == '自选商品'">
          <pagination :total="page_data.total_page" @pageChange="pageChange"></pagination>
        </div>
        <div class="m-bottom-btn m-flex-center">
            <span class="m-btn" @click="lastStep">上一步</span>
            <span class="m-btn  active" @click="storeSubmit">完成</span>
        </div>
      </div>
    </el-form>
  </div>
</template>

<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  import step from '../../components/common/step';
  import Pagination from "../../components/common/page";
  import api from '../../api/api';
  import axios from 'axios';
  export default {
    data() {
      return {
        title_list:[
          {
            name:'店铺活动',
            url:'/activity/storeActivity'
          },
          {
            name:'创建/编辑活动',
            url:'/activity/activityStoreStepThree'
          }
        ],
        step:[
          {
            name:'基本信息',
            active:true,
            next:true
          },
          {
            name:'优惠门槛及内容',
            active:true,
            next:true
          },
          {
            name:'设置商品优惠',
            active:true,
            next:false
          }
        ],
        storeForm:{
          name:'',
          status:''
        },
        rules:{
          ACbrand:[
            { required: true, message: '请选择优惠类型', trigger: 'blur' }
          ],
        },
        radio:'1',
        product_data:[],
        page_data:{
          total_page:0,
          current_page:1,
          total_num:0,
          page_size:10,
        },
        check_data:[]
      }
    },
    components:{
      pageTitle,
      step,
      Pagination
    },
    mounted(){
      let item = this.$store.state.activity;
      if(!item.COname || !item.COabo || !item.COstart || !item.COend){
        this.$message({
          type:'warning',
          message:'请先填写第一步内容',
          duration:1000
        });
        this.$router.push('/activity/activityStoreStepOne');
        return false;
      }
      if(!item.COfilter || !(item.COdiscount || item.COamount || item.COtype == '其它')){
        this.$message({
          type:'warning',
          message:'请先填写第二步内容',
          duration:1000
        });
        this.$router.push('/activity/activityStoreStepTwo');
        return false;
      }
      this.getData();
    },
    methods: {
      /*获取表格数据*/
      getData(v,code){
        let that = this;
        let params = {
          token:localStorage.getItem('token'),
          PBstatus:this.storeForm.status,
          page_num: v || this.page_data.current_page,
          page_size:this.page_data.page_size,
          product_filter:code || ''
        };
        axios.get(api.get_all_product,{params:params}).then(res => {
          if(res.data.status == 200) {
            this.product_data = res.data.data.products;
            for(let i=0;i<this.product_data.length;i++){
              if(this.$store.state.activity.PRids.indexOf(this.product_data[i].PRid)!= -1){
                that.$nextTick(function(){//注意这个，延时执行。
                  that.$refs.table.toggleRowSelection(that.product_data[i],true);//每次更新了数据，触发这个函数即可。
                });
              }
            }
            this.page_data.total_num = res.data.data.count;
            this.page_data.total_page = Math.ceil(this.page_data.total_num / this.page_data.page_size);
          }else{
            this.$message.error(res.data.message);
          }
        },error => {
          this.$message.error(error.data.message);
        })
      },
      freshClick(){
        console.log('fresh');
      },
      /*搜索商品*/
      onSubmit(){
        this.getData(1,this.storeForm.name);
      },
      /*表格多选事件*/
      changeFun(e){
        let _arr = [];
       for(let i=0;i<e.length;i++){
         _arr.push(e[i].PRid);
       }
        this.check_data[this.page_data.current_page-1] = [].concat(_arr);
        let newarr=[];
        let arr = JSON.parse(JSON.stringify(this.check_data));
        for(let i=0;i<arr.length;i++)
        {
          newarr=newarr.concat(arr[i]);
        }
        this.$store.state.activity.PRids = [].concat(newarr);
      },
      /*完成*/
      storeSubmit(){
        if(this.$route.query.COid){
          this.$message({
            type: 'warning',
            message: '已创建过的活动不可修改'
          });
          return false;
        }
        // console.log(this.$store.state.activity)
        let _form = JSON.parse(JSON.stringify(this.$store.state.activity));
        // for(let i =0;i<this.$store.state.activity.COimage.length;i++){
        //   _form.COimage = this.$store.state.activity.COimage[0].url
        // }
        if(_form.COtype == '其它'){
          _form.COother = (_form.COotherType == 0 && _form.COotherContent[0] == '') ? '包邮':_form.COotherContent[_form.COotherType]
        }
        _form.COamount = Number(_form.COamount);
        _form.COnumber = Number(_form.COnumber);
        _form.COfilter  = Number(_form.COfilter );
        _form.COdiscount = Number(_form.COdiscount);

        axios.post(api.create+'?token='+localStorage.getItem('token'),_form).then(res => {
          if(res.data.status == 200){
            this.$message({
              type: 'success',
              message: '处理成功 '
            });
            this.$store.state.activity = {
              COabo:'',
              COname:'',
              COstatus:'',
              COstart:'',
              COend:'',
              COfilter:null,
              COother:'',
              COdiscount:null,
              COamount:null,
              COtype:'满减',
              COunit:'元',
              COnumber:null,
              COimage:[],
              COotherType:'0',
              COotherContent:[
                '','',''
              ],
              COproduct:'全店商品',
              PRids:[],
              COgenre:'活动'
            };
            this.$router.push('/activity/storeActivity');
          }else{
            this.$message({
              type: 'error',
              message: '服务器请求失败，请稍后再试 '
            });
          }
        },error =>{
          this.$message({
            type: 'error',
            message: '服务器请求失败，请稍后再试 '
          });
        })
      },
      lastStep(){
        this.$router.push('/activity/activityStoreStepTwo')
      },
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
