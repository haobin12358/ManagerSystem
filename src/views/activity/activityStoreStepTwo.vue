<template>
  <div class="m-step">
    <page-title :list="title_list" @freshClick="freshClick"></page-title>
    <el-form  :model="$store.state.activity"  :rules="rules" label-width="1.2rem" class="demo-ruleForm" :disabled="$store.state.activity.disabled" >
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
            <table class="m-activity-table">
              <tr>
                <td width="250">活动描述：<span>{{$store.state.activity.COabo}}</span></td>
                <td>活动时间：<span>{{$store.state.activity.COstart}} 至 {{$store.state.activity.COend}}</span></td>
              </tr>
              <tr>
                <td>活动类型：<span>{{$store.state.activity.COtype}}</span></td>
                <td>活动预热：<span>预热</span></td>
              </tr>
            </table>
          </div>
        </div>
        <div class="m-step-part">
          <h4>基本信息</h4>
          <el-form-item label="优惠类型：" prop="COtype">
            <p class="m-alert-box">
              <el-radio v-model="$store.state.activity.COtype" label="满折">满折（打折）</el-radio>
              <span class="m-alert-icon"></span>
              <span class="m-alert-info">设置折扣前请务必确保您的折扣基准价是法律规定的原价（前七天最低价，详见《淘宝价格发布规范》 ），若不是，请您返回商品发布页对价格进行修改，否则由此产生的价格欺诈等法律责任需由您自行承担。</span>
            </p>
            <p>
              <el-radio v-model="$store.state.activity.COtype" label="满减">满元（减钱）</el-radio>
            </p>
            <p class="m-margin-bottom">
              <el-radio v-model="$store.state.activity.COtype" label="其它">其它</el-radio>
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
              <h4>优惠门槛及内容</h4>
              <el-form-item label="优惠门槛：" prop="COfilter">
                <span>满&nbsp;</span>
                <el-input v-model="$store.state.activity.COfilter" type="number" class="m-input-s" placeholder=""></el-input>
                <el-radio v-model="$store.state.activity.COunit" label="元">元</el-radio>
                <el-radio v-model="$store.state.activity.COunit" label="件">件</el-radio>
              </el-form-item>
              <el-form-item label="优惠内容：" prop="COunit">
                <div v-if="$store.state.activity.COtype == '满折'">
                  <p class="m-alert-box">
                    <!--<el-radio v-model="radio" label="1">打</el-radio>-->
                    <span>打</span>
                    <el-input v-model="$store.state.activity.COdiscount" type="number" class="m-input-s" placeholder="值为0-1之间"></el-input>
                    <span>&nbsp;折</span>
                    <span class="m-alert-icon"></span>
                    <span class="m-alert-info m-alert-info-a">设置折扣前请务必确保您的折扣基准价是法律规定的原价（前七天最低价，详见《淘宝价格发布规范》 ），若不是，请您返回商品发布页对价格进行修改，否则由此产生的价格欺诈等法律责任需由您自行承担。</span>
                  </p>
                </div>
                <div v-if="$store.state.activity.COtype == '满减'">
                  <p class="m-alert-box">
                    <!--<el-radio v-model="radio" label="3">减</el-radio>-->
                    <span>减</span>
                    <el-input v-model="$store.state.activity.COamount" type="number" class="m-input-s" placeholder=""></el-input>
                    <span>&nbsp;元</span>
                    <span class="m-alert-icon"></span>
                    <span class="m-alert-info m-alert-info-a">设置折扣前请务必确保您的折扣基准价是法律规定的原价（前七天最低价，详见《淘宝价格发布规范》 ），若不是，请您返回商品发布页对价格进行修改，否则由此产生的价格欺诈等法律责任需由您自行承担。</span>
                  </p>
                </div>
               <div v-if="$store.state.activity.COtype == '其它'" class="m-radio-p">
                 <p>
                   <el-radio v-model="$store.state.activity.COotherType" label="0">包邮</el-radio>
                   <el-input v-model="$store.state.activity.COotherContent[0]" class="m-input-m" placeholder="备注" v-if="$store.state.activity.COotherType ==0"></el-input>
                 </p>
                 <p>
                   <el-radio v-model="$store.state.activity.COotherType" label="1">送赠品</el-radio>
                   <el-input v-model="$store.state.activity.COotherContent[1]" class="m-input-m" placeholder="赠品内容" v-if="$store.state.activity.COotherType ==1"></el-input>
                 </p>
                 <!--<p>-->
                   <!--<el-radio v-model="radio" label="2">送权益</el-radio>-->
                   <!--<el-input v-model="storeForm.name" class="m-input-m" placeholder="权益内容"></el-input>-->
                 <!--</p>-->
                 <p>
                   <el-radio v-model="$store.state.activity.COotherType" label="2">送优惠券</el-radio>
                   <!--<el-input v-model="storeForm.name" class="m-input-m" placeholder="优惠券内容"></el-input>-->
                   <el-select v-model="$store.state.activity.COotherContent[2]" filterable remote :remote-method="productBlur" placeholder="选择已有优惠券" class="m-input-l" v-if="$store.state.activity.COotherType ==2">
                     <el-option
                       v-for="(items,index) in discount_data"
                       :key="index"
                       :label="items.COname"
                       :value="items.COid"></el-option>
                   </el-select>
                   <span class="m-link m-first" @click="addNewDiscount" v-if="$store.state.activity.COotherType == 2">新增优惠券</span>
                 </p>
               </div>

                <!--<p class="m-alert-btn-box">-->
                  <!--<span class="m-alert-btn active" @click="addLayer">+增加一级优惠</span>-->
                  <!--<span class="m-alert-btn" @click="cutLayer(index)">删除一级优惠</span>-->
                <!--</p>-->
              </el-form-item>
            </div>
          </template>


        </div>
        <div class="m-bottom-btn m-flex-center">
            <span class="m-btn" @click="lastStep">上一步</span>
            <span class="m-btn  active" @click="onSubmit">下一步</span>
        </div>
      </div>
    </el-form>
  </div>
</template>

<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  import step from '../../components/common/step';
  import axios from 'axios';
  import api from '../../api/api';
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
          COtype:[
            { required: true, message: '请输入活动优惠类型', trigger: 'blur' }
          ],
          COfilter:[
            { required: true, message: '请输入优惠门槛', trigger: 'blur' }
          ],
          COunit:[
            { required: true, message: '请选择优惠内容', trigger: 'blur' }
          ],
          ACend:[
            { required: true, message: '请选择结束时间', trigger: 'blur' }
          ],
          ACbrand:[
            { required: true, message: '请选择优惠类型', trigger: 'blur' }
          ],
        },
        discount_data:[]
      }
    },
    components:{
      pageTitle,
      step
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
      if(this.$route.query.COid){
        this.$store.state.activity.COotherContent[2] = this.$route.query.COid;
      }
      this.getData();
    },
    methods: {
      /*获取所有优惠券数据*/
      getData(){
        let params = {
          token:localStorage.getItem('token'),
          page_num: 1,
          page_size:100,
          COgenre:'优惠券'
        };
        axios.get(api.get_all_card,{params:params}).then(res => {
          if(res.data.status == 200) {
            this.discount_data = res.data.CouponsActives;
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
      /**新增活动层级*/
      addLayer(){
        this.layer_data.push(1);
      },
      /*删除优惠层级*/
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
      /*下一步*/
      onSubmit(){
        this.$router.push('/activity/activityStoreStepThree?COid='+this.$route.query.COid);
      },
      /*上一步*/
      lastStep(){
        this.$router.push('/activity/activityStoreStepOne');
      },
      /*新增优惠券*/
      addNewDiscount(){
        this.$router.push('/activity/discountStoreStepOne?router=activity');
      }
    }
  }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/activity";
.m-radio-p{
  p{
    margin-bottom: 0.2rem;
  }
}
</style>
