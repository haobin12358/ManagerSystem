<template>
  <div class="m-step">
    <page-title :list="title_list" @freshClick="freshClick"></page-title>
    <el-form  :model="storeForm" ref="storeForm" :rules="rules" label-width="1.2rem" class="demo-ruleForm">
      <div class="m-step-content">
        <h3 class="m-step-title">创建新活动</h3>
        <div class="m-step-part">
          <step :list="step"></step>
        </div>
        <div class="m-step-part">
          <h3 class="m-step-h3 m-flex-between">
            <span>活动名称：2565484102</span>
          </h3>
          <div>
            <table class="m-activity-table" width="100%">
              <tr>
                <td width="250">活动描述：<span>新品秒杀价</span></td>
                <td width="400">活动时间：<span>2018-06-29  00 : 00：01 至 2018-06-29  23 : 59：59</span></td>
                <td width="320">活动预热：<span>不预热</span></td>
              </tr>
              <tr>
                <td>活动类型：<span>自选商品</span></td>
                <td>创建时间：<span>2018-06-29  00 : 00：01 </span></td>
              </tr>
            </table>
          </div>
        </div>
        <el-form-item label="优惠类型：" prop="ACbrand">
          <p>
            <el-radio v-model="$store.state.activity.ACbrand" label="1">自选商品</el-radio>
          </p>
          <p>
            <el-radio v-model="$store.state.activity.ACbrand" label="2">全店商品</el-radio>
          </p>
        </el-form-item>
        <el-form :inline="true" :model="storeForm" class="demo-form-inline" v-if=" $store.state.activity.ACbrand == '1'">
          <div class="m-select-box">
            <div class="m-left">
              <el-form-item label="商品名称">
                <el-input v-model="storeForm.name" class="m-input-s" placeholder=""></el-input>
              </el-form-item>
              <el-form-item label="商品ID">
                <el-input v-model="storeForm.name" class="m-input-s" placeholder=""></el-input>
              </el-form-item>
              <el-form-item label="商品状态">
                <el-select v-model="storeForm.name" class="m-input-s" placeholder="活动区域">
                  <el-option label="区域一" value="shanghai"></el-option>
                  <el-option label="区域二" value="beijing"></el-option>
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
        <div class="m-middle" style="width: 100%;margin-top: 0.1rem;" v-if=" $store.state.activity.ACbrand == '1'">
          <el-table :data="product_data" stripe style="width: 100%">
            <el-table-column type="selection" width="55"></el-table-column>
            <el-table-column align="center" prop="userId" width="400" label="宝贝描述">
              <template slot-scope="scope">
                <div class="m-production-description">
                  <p class="m-img"></p>
                  <div>
                    <p>商品1</p>
                    <p>ID:5489798456151241</p>
                  </div>
                </div>
              </template>
            </el-table-column>
            <el-table-column align="center" prop="userId" label="价格" ></el-table-column>

            <el-table-column align="center" prop="loginTime" label="库存" ></el-table-column>
            <!--<el-table-column align="center" label="操作" >-->
              <!--<template slot-scope="scope">-->
                <!--<span class="m-link m-first">参加活动</span>-->
              <!--</template>-->
            <!--</el-table-column>-->
          </el-table>
        </div>
        <div class="m-page-box">
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
          date1:''
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
        }
      }
    },
    components:{
      pageTitle,
      step,
      Pagination
    },
    methods: {
      freshClick(){
        console.log('fresh');
      },
      onSubmit(){

      },
      storeSubmit(){

      },
      lastStep(){
        this.$router.push('/activity/activityStoreStepTwo')
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
        // this.getData(v);
      }
    },
    created() {

    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/activity";

</style>
