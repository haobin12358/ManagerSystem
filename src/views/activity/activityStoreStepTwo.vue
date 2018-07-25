<template>
  <div class="m-step">
    <page-title :list="title_list" @freshClick="freshClick"></page-title>
    <el-form  :model="storeForm" label-width="1.2rem" >
      <div class="m-step-content">
        <h3 class="m-step-title">创建新活动</h3>
        <div class="m-step-part">
          <step :list="step"></step>
        </div>
        <div class="m-step-part">
          <h3 class="m-step-h3 m-flex-between">
            <span>活动编号：2565484102</span>
          </h3>
          <div>
            <table class="m-activity-table">
              <tr>
                <td width="250">活动名称：<span>第二件6折</span></td>
                <td>活动时间：<span>2018-06-29  00 : 00：01 至 2018-06-29  23 : 59：59</span></td>
              </tr>
              <tr>
                <td>活动类型：<span>自选商品</span></td>
                <td>活动预热：<span>不预热</span></td>
              </tr>
            </table>
          </div>
        </div>
        <div class="m-step-part">
          <h4>基本信息</h4>
          <el-form-item label="优惠类型：">
            <p class="m-alert-box">
              <el-radio v-model="storeForm.ACtype" label="1">满减（打折）</el-radio>
              <span class="m-alert-icon"></span>
              <span class="m-alert-info">设置折扣前请务必确保您的折扣基准价是法律规定的原价（前七天最低价，详见《淘宝价格发布规范》 ），若不是，请您返回商品发布页对价格进行修改，否则由此产生的价格欺诈等法律责任需由您自行承担。</span>
            </p>
            <p>
              <el-radio v-model="storeForm.ACtype" label="2">满元（减钱）</el-radio>
            </p>
            <p class="m-margin-bottom">
              <el-radio v-model="storeForm.ACtype" label="3">其它</el-radio>
            </p>
          </el-form-item>
          <!--<el-form-item label="开始时间：">-->
            <!--<el-date-picker type="date"  placeholder="起始时间" v-model="storeForm.date1" style="width: 2rem;"></el-date-picker>-->
          <!--</el-form-item>-->
          <!--<el-form-item label="结束时间：">-->
            <!--<el-date-picker type="date"  placeholder="结束时间" v-model="storeForm.date1" style="width: 2rem;"></el-date-picker>-->
          <!--</el-form-item>-->

          <template v-for="(item,index) in layer_data">
            <div>
              <h4>优惠门槛及内容——层级{{index+1}}</h4>
              <el-form-item label="优惠门槛：">
                <span>满&nbsp;</span>
                <el-input v-model="storeForm.name" class="m-input-s" placeholder=""></el-input>
                <el-radio v-model="radio" label="3">件</el-radio>
                <el-radio v-model="radio" label="1">元</el-radio>
              </el-form-item>
              <el-form-item label="优惠内容：">
                <div v-if="storeForm.ACtype == 1">
                  <p class="m-alert-box">
                    <el-radio v-model="radio" label="1">打</el-radio>
                    <el-input v-model="storeForm.ACdiscount" class="m-input-s" placeholder="值为0-1之间"></el-input>
                    <span>&nbsp;折</span>
                    <span class="m-alert-icon"></span>
                    <span class="m-alert-info m-alert-info-a">设置折扣前请务必确保您的折扣基准价是法律规定的原价（前七天最低价，详见《淘宝价格发布规范》 ），若不是，请您返回商品发布页对价格进行修改，否则由此产生的价格欺诈等法律责任需由您自行承担。</span>
                  </p>
                </div>
                <div v-if="storeForm.ACtype == 2">
                  <p class="m-alert-box">
                    <el-radio v-model="radio" label="3">减</el-radio>
                    <el-input v-model="storeForm.ACamount" class="m-input-s" placeholder=""></el-input>
                    <span>&nbsp;元</span>
                    <span class="m-alert-icon"></span>
                    <span class="m-alert-info m-alert-info-a">设置折扣前请务必确保您的折扣基准价是法律规定的原价（前七天最低价，详见《淘宝价格发布规范》 ），若不是，请您返回商品发布页对价格进行修改，否则由此产生的价格欺诈等法律责任需由您自行承担。</span>
                  </p>
                </div>
               <div v-if="storeForm.ACtype == 3">
                 <p>
                   <el-radio v-model="radio" label="2">包邮</el-radio>
                   <el-input v-model="storeForm.name" class="m-input-m" placeholder="备注"></el-input>
                 </p>
                 <p>
                   <el-radio v-model="radio" label="2">送赠品</el-radio>
                   <el-input v-model="storeForm.name" class="m-input-m" placeholder="赠品内容"></el-input>
                 </p>
                 <p>
                   <el-radio v-model="radio" label="2">送权益</el-radio>
                   <el-input v-model="storeForm.name" class="m-input-m" placeholder="权益内容"></el-input>
                 </p>
                 <p>
                   <el-radio v-model="radio" label="2">送优惠券</el-radio>
                   <el-input v-model="storeForm.name" class="m-input-m" placeholder="优惠券内容"></el-input>
                 </p>
               </div>

                <p class="m-alert-btn-box">
                  <span class="m-alert-btn active" @click="addLayer">+增加一级优惠</span>
                  <span class="m-alert-btn" @click="cutLayer(index)">删除一级优惠</span>
                </p>
              </el-form-item>
            </div>
          </template>


        </div>
        <div class="m-bottom-btn m-flex-center">
          <router-link to="/activity/activityStoreStepOne" >
            <span class="m-btn">上一步</span>
          </router-link>
          <router-link to="/activity/activityStoreStepThree" >
            <span class="m-btn  active">下一步</span>
          </router-link>
        </div>
      </div>
    </el-form>
  </div>
</template>

<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  import step from '../../components/common/step';
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
            url:'/activity/activityStoreStepTwo'
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
            next:false
          },
          {
            name:'设置商品优惠',
            active:false,
            next:false
          }
        ],
        layer_data:[1],
        storeForm:{
          name:'',
          date1:'',
          ACtype:'1',
          ACdiscount:0.8,
          ACamount:''
        },
        rules:{
          ACtype:[
            { required: true, message: '请输入活动优惠类型', trigger: 'blur' }
          ],
          ACabo:[
            { required: true, message: '请输入活动描述', trigger: 'blur' }
          ],
          ACstart:[
            { required: true, message: '请选择开始时间', trigger: 'blur' }
          ],
          ACend:[
            { required: true, message: '请选择结束时间', trigger: 'blur' }
          ],
          ACbrand:[
            { required: true, message: '请选择优惠类型', trigger: 'blur' }
          ],
        },
        radio:'1'
      }
    },
    components:{
      pageTitle,
      step
    },
    methods: {
      freshClick(){
        console.log('fresh');
      },
      addLayer(){
        this.layer_data.push(1);
      },
      cutLayer(v){
        if(this.layer_data.length <=1 ){
          this.$message({
            type: 'warning',
            message: '默认至少一个层级'
          });
          return false;
        }
        this.$confirm('此操作将永久删除该层级, 是否继续?', '提示', {
          confirmButtonText: '确定',
          cancelButtonText: '取消',
          type: 'warning'
        }).then(() => {
          this.layer_data.splice(v,1);
          this.$message({
            type: 'success',
            message: '删除成功!'
          });
        }).catch(() => {
          this.$message({
            type: 'info',
            message: '已取消删除'
          });
        });
      },
      onSubmit(){

      }
    },
    created() {

    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/activity";

</style>
