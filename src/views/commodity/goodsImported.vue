<template>
<div class="m-goodsImported">
  <el-form ref="form" :model="form" :rules="rules" label-width="1.2rem" class="demo-ruleForm">
    <page-title :title="name" @freshClick="freshClick"></page-title>
    <div class="m-goodsImported-content">
      <div class="m-edit-btn">
        <span>-编辑-</span>
      </div>
      <a name="basicInfo"></a>
      <div class="m-one-part">
        <h3 id="basicInfo">基本信息</h3>
        <el-form-item label="商品名称:" prop="PRname">
          <el-input v-model="form.PRname" class="m-input-l" ></el-input>
        </el-form-item>
        <el-form-item label="添加描述:" prop="PRinfo">
          <el-input v-model="form.PRinfo" class="m-input-l" ></el-input>
          <p class="m-alert">建议描述文字在36字以内</p>
        </el-form-item>
        <el-form-item label="商品属性:" prop="PRbrand">
          <div class="m-select-box">
            <p class="m-alert">错误填写商品属性，可能会引起商品下架或搜索流量减少，影响您的正常销售，请认真准确填写！</p>
            <div class="m-selects">
              <template v-for="(item,index) in brand_list">
                <div v-if="item.CBvalue == ''"  class="m-form-item">
                  <span class=" m-label">{{item.CBname}}</span>
                  <el-input v-model="form.PRbrand[index]" class="m-input-s" ></el-input>
                </div>
                <div  class="m-form-item" >
                  <span class=" m-label">{{item.CBname}}</span>
                  <el-select v-model="form.PRbrand[index]" clearable class="m-input-s" >
                    <el-option
                      v-for="items in item.CBvalue"
                      :key="items"
                      :label="items"
                      :value="items"></el-option>
                  </el-select>
                </div>
              </template>
            </div>
          </div>
        </el-form-item>
        <el-form-item label="商品照片:" prop="PRimage">
          <el-upload
            action="http://120.79.182.43:7443/sharp/manager/other/upload_files"
            list-type="picture-card"
            :on-preview="handlePictureCardPreview"
            :on-remove="handleRemove"
          class="m-img-l"
            :limit="5"
            :on-exceed="outImg">
            <span>+添加图片</span>
          </el-upload>
          <el-dialog :visible.sync="dialogVisible">
            <img width="100%" :src="form.PRimage" alt="">
          </el-dialog>
          <p class="m-img-p">建议尺寸：700*700像素，可以通过拖动图片调整前后顺序，最多上传5张商品图片</p>
        </el-form-item>

        <el-form-item label="商品样式及价格:" prop="brands">
          <div class="m-product-style">
            <div>
              <span class="m-img-label">A:</span> <el-input v-model="form.brands_key[0]" placeholder="输入商品属性" class="m-input-s" ></el-input>
              <span class="m-img-label">B:</span> <el-input v-model="form.brands_key[1]" placeholder="输入商品属性" class="m-input-s" ></el-input>
            </div>
            <div class="m-product" v-for="(item,index) in brands">
              <div class="m-product-input">
                <div>
                  <span class="m-img-label">A:</span>
                  <el-input v-model="form.brands[index].BRands[0]" placeholder="输入商品颜色，如粉红色" class="m-input-m" ></el-input>
                </div>
                <div>
                  <span class="m-img-label">B:</span>
                  <el-input v-model="form.brands[index].BRands[1]" placeholder="输入商品规格，如进阶版" class="m-input-m" ></el-input>
                </div>
                <div>
                  <span class="m-img-label">价格:</span>
                  <el-input v-model="form.brands[index].PBprice" placeholder="输入商品该规格价格" class="m-input-m" ></el-input>
                </div>
                <div>
                  <span class="m-img-label">库存:</span>
                  <el-input v-model="form.brands[index].PBnumber" placeholder="输入商品该规格库存" class="m-input-m" ></el-input>
                  <p class="m-alert" style="margin-left: 0.6rem;">库存为0时，会放入已售罄列表中</p>
                </div>
              </div>
              <div>
                <el-upload
                  action="https://jsonplaceholder.typicode.com/posts/"
                  list-type="picture-card"
                  :on-preview="handlePictureCardPreview"
                  class="m-img-xl"
                  :limit="1"
                  :on-exceed="outImg"
                  :on-success="imgUp">
                  <span>+添加图片</span>
                </el-upload>
                <!--<el-dialog :visible.sync="!form.brands[index].PBimage">-->
                  <!--<img width="100%" :src="form.brands[index].PBimage" alt="">-->
                <!--</el-dialog>-->
              </div>
              <div>
                <span class="m-delete" @click="deleteOne(index)">删除</span>
              </div>
            </div>
            <p class="m-add-more" @click="addMore">+查看更多</p>
            <p class="m-look-more" @click="showMore('show_basic_info')">更多基本信息设置</p>
          </div>
        </el-form-item>
        <div v-show="show_basic_info">
          <el-form-item label="商品卖点:" :rules="[{ required: false, message: '年龄不能为空'}, { type: 'number', message: '年龄必须为数字值'}]">
            <el-input v-model="form.name" class="m-input-l" placeholder="输入内容"></el-input>
            <p class="m-alert">在商品详情页下面展示卖点信息，建议36字以内</p><!--，<span class="m-link">查看示例</span>-->
          </el-form-item>
          <el-form-item label="商品视频:" :rules="[{ required: false, message: '年龄不能为空'},{ type: 'number', message: '年龄必须为数字值'}]">
            <el-upload
              action="https://jsonplaceholder.typicode.com/posts/"
              list-type="picture-card"
              :on-preview="handlePictureCardPreview"
              :on-remove="handleRemove"
              class="m-img-l">
              <span>+添加视频</span>
            </el-upload>
            <el-dialog :visible.sync="dialogVisible">
              <img width="100%" :src="dialogImageUrl" alt="">
            </el-dialog>
            <p class="m-img-p">建议视频尺寸比例为1:1或16:9，时长不超过60秒</p>
          </el-form-item>
          <el-form-item label="商品详情:" :rules="[{ required: false, message: '年龄不能为空'},{ type: 'number', message: '年龄必须为数字值'}]">
            <el-upload
              action="https://jsonplaceholder.typicode.com/posts/"
              list-type="picture-card"
              :on-preview="handlePictureCardPreview"
              :on-remove="handleRemove"
              class="m-img-l">
              <span>+添加图片</span>
            </el-upload>
            <el-dialog :visible.sync="dialogVisible">
              <img width="100%" :src="dialogImageUrl" alt="">
            </el-dialog>
            <p class="m-img-p">建议尺寸：700*700像素，可以通过拖动图片调整前后顺序</p>
          </el-form-item>
        </div>

      </div>
      <a name="priceInfo"></a>
      <div class="m-one-part">
        <h3 id="priceInfo">商品库存</h3>
        <el-form-item label="划线价格:" :rules="[{ required: false, message: '年龄不能为空'}, { type: 'number', message: '年龄必须为数字值'}]">
          <el-input v-model="form.name" class="m-input-m" ></el-input>
          <p class="m-alert">建议描述文字在36字以内</p>
        </el-form-item>
        <el-form-item label="库存:" :rules="[{ required: false, message: '年龄不能为空'}, { type: 'number', message: '年龄必须为数字值'}]">
          <el-input v-model="form.name" class="m-input-m" ></el-input>
          <div class="m-check-content">
            <el-checkbox v-model="checked"></el-checkbox>
            <span>商品详情不显示剩余件数</span>
          </div>
          <p class="m-alert">库存为0时，会放入已售罄列表中</p>
          <p class="m-look-more" @click="showMore('show_price_info')">更多价格库存设置</p>
        </el-form-item>
        <div v-show="show_price_info">
          <el-form-item label="成本价格:" :rules="[{ required: false, message: '年龄不能为空'}, { type: 'number', message: '年龄必须为数字值'}]">
            <el-input v-model="form.name" class="m-input-m" ></el-input>
            <p class="m-alert">建议描述文字在36字以内</p>
          </el-form-item>
        </div>


      </div>

      <a name="otherInfo"></a>
      <div class="m-one-part m-other">
        <h3 id="otherInfo">其他信息</h3>
        <el-form-item label="快递运费:" prop="PRfrankingR">
          <el-switch
            v-model="form.PRfrankingR"
            active-color="#9fd0bf"
            inactive-color="#dbdcdc">
          </el-switch>
          <span class="m-switch-label">统一邮费</span>
          <!--<el-radio v-model="form.PRfrankingR" label="">统一邮费  </el-radio>-->
          <el-input v-model="form.PRfranking" class="m-input-s" ></el-input>
        </el-form-item>
        <el-form-item label="上架时间:" :rules="[{ required: true, message: '年龄不能为空'},{ type: 'number', message: '年龄必须为数字值'}]">
          <div>
            <el-radio v-model="radio" label="1">立即上架售卖  </el-radio>
          </div>
          <div>
            <el-radio v-model="radio" label="0">自定义上架时间  </el-radio>
            <el-input v-model="form.name" class="m-input-s" ></el-input>
            <p class="m-alert">需等待管理员审批完成，上架时间请选择24小时以后</p>
          </div>
          <p class="m-look-more" @click="showMore('show_other_info')">更多其他信息设置</p>
        </el-form-item>
        <div v-show="show_other_info">
          <el-form-item label="限购:" :rules="[{ required: false, message: '年龄不能为空'},{ type: 'number', message: '年龄必须为数字值'}]">
            <div>
              <el-radio v-model="radio" label="1">无现货，下单后需过段时间才能发货  </el-radio>
            </div>
            <div>
              <el-radio v-model="radio" label="0">只允许特定用户购买  </el-radio>
            </div>
            <div>
              <el-radio v-model="radio" label="0">允许用户购买数量  </el-radio>
              <el-input v-model="form.name" class="m-input-s" placeholder="每个ID限购5个"></el-input>
            </div>
          </el-form-item>
        </div>

      </div>

      <div class="m-goodsImported-foot">
        <el-button type="primary" class="m-foot-btn" @click="submitClick">保存</el-button>
        <el-button type="primary" class="m-foot-btn" @click="submitClick">发布</el-button>
      </div>
    </div>
    <div class="m-right-side">
      <div class="m-step-box">
        <ul>
          <li>
            <span class="circle m-both-ends"></span>
            <span class="m-step-content"></span>
          </li>
          <li>
            <span class="line">|</span>
            <span class="m-step-content"></span>
          </li>
          <li @click="sideClick('basicInfo')">
            <!--<a href="#basicInfo">-->
              <span class="circle" :class="linkTo == 'basicInfo'?'active':''"></span>
              <span class="m-step-content">1、基本信息</span>
            <!--</a>-->
          </li>
          <li>
            <span class="line">|</span>
            <span class="m-step-content"></span>
          </li>
          <li @click="sideClick('priceInfo')">
            <!--<a href="#priceInfo">-->
              <span class="circle" :class="linkTo == 'priceInfo'?'active':''"></span>
              <span class="m-step-content">2、商品库存</span>
            <!--</a>-->
          </li>
          <li>
            <span class="line">|</span>
            <span class="m-step-content"></span>
          </li>
          <li @click="sideClick('otherInfo')">
            <!--<a href="#otherInfo">-->
              <span class="circle " :class="linkTo == 'otherInfo'?'active':''"></span>
              <span class="m-step-content">3、其他信息</span>
            <!--</a>-->
          </li>
          <li>
            <span class="line">|</span>
            <span class="m-step-content"></span>
          </li>
          <li>
            <span class="circle m-both-ends"></span>
            <span class="m-step-content"></span>
          </li>
        </ul>
      </div>
      <div class="m-side-btn">
        <span class="m-btn" @click="submitClick">保存</span>
      </div>
    </div>
  </el-form>
</div>

</template>
<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  import axios from 'axios';
  import api from '../../api/api';
  import {Message} from 'element-ui';
    export default {
        data() {
            return {
              name:'商品发布',
              form:{
                CTid:0,
                PRname:'',
                PRinfo:'',
                PRbrand:[],
                PRimage:'xxxx',
                brands_key:['',''],
                brands:[{
                  PBprice:'',
                  PBunit:'$',
                  PBimage:'xxxx',
                  BRands:['',''],
                  PBnumber:''
                }],
                PRvideo:'',
                PRaboimage:'',
                PRfrankingR:true,
                PRfranking:''
              },
              rules:{
                PRname:[
                  { required: true, message: '请输入商品名称', trigger: 'blur' }
                ],
                PRinfo:[
                  { required: true, message: '请添加商品描述', trigger: 'blur' }
                ],
                PRbrand:[
                  { required: true, message: '请选择属性', trigger: 'blur' }
                ],
                PRimage:[
                  { required: true, message: '请上传照片', trigger: 'blur' }
                ],
                brands_key:'',
                brands:[
                  { required: true, message: '请填写商品样式及价格', trigger: 'blur' }
                ],
                PRfrankingR:[
                  { required: true, message: '请设置邮费', trigger: 'blur' }
                ],
              },
              brand_one:{
                PBprice:'',
                PBunit:'$',
                PBimage:'zcxcz',
                BRands:['',''],
                PBnumber:''
              },
              brand_list:[],
              brands:[{
                PBprice:'',
                PBunit:'$',
                PBimage:'',
                BRands:['',''],
                PBnumber:''
              }],
              dialogImageUrl: '',
              dialogVisible: false,
              checked:true,
              radio:0,
              linkTo:'basicInfo',
              show_basic_info:false,
              show_price_info:false,
              show_other_info:false
            }
        },
      components:{
        pageTitle
      },
        methods: {
          getCategorybrands(id){
            let that = this;
            axios.get(api.get_categorybrands,{params:{
                CTid:id,
                token:localStorage.getItem('token')
              }}).then(res => {
                if(res.data.status == 200){
                  that.brand_list = res.data.data;
                }else{
                  that.$message.error(res.data.message)
                }
            },error => {
              that.$message.error(error.data.message)
            })
          },
          freshClick(){
            console.log('fresh');
          },
          handleRemove(file, fileList) {
            console.log(file, fileList);
          },
          handlePictureCardPreview(file) {
            this.form.PRimage = file.url;
            this.dialogVisible = true;
          },
          sideClick(v){
            this.linkTo = v;
            if(v == 'basicInfo'){
              document.documentElement.scrollTop = 96;
            }else if(v == 'priceInfo'){
              document.documentElement.scrollTop = document.getElementById('priceInfo').offsetTop - 89;
            }else if(v == 'otherInfo'){
              document.documentElement.scrollTop = document.getElementById('otherInfo').offsetTop - 229;
            }
          },
          handleScroll(){
            if(document.getElementById('otherInfo') && document.getElementById('priceInfo') ){
              if((document.getElementById('otherInfo').offsetTop <= document.documentElement.scrollTop + 230 ) ){
                this.linkTo = 'otherInfo';
              }else if((document.getElementById('priceInfo').offsetTop < document.documentElement.scrollTop +90  ) &&  (document.getElementById('otherInfo').offsetTop > document.documentElement.scrollTop +230)){
                this.linkTo = 'priceInfo'
              }else{
                this.linkTo = 'basicInfo'
              }
            }else{
              return
            }

          },
          //显示更多
          showMore(v){
            this[v] = !this[v];
          },
          //  发布
          issueClick(){
            this.$router.push('/commodity/commodityManagement')
          },
          imgUp(response, file, fileList){
            console.log(response)
          },
          submitClick(){
            let that = this;

            this.$refs['form'].validate((valid) => {
                if (valid) {
                  that.query(this.form)
                }
            })
          },
          query(params){
            let _brands = [];
            let _form = JSON.parse(JSON.stringify(params))
            for(let i=0;i<this.form.PRbrand.length;i++){
              if(_form.PRbrand[i] != undefined){
                let _value = this.brand_list[i];
                _value.CBvalue = _form.PRbrand[i];
                _brands.push(_value);
              }
            }
            _form.PRbrand = _brands;
            axios.post(api.release_product+'?token='+localStorage.getItem('token'),_form).then(res => {
              if(res.data.status == 200){
                this.$message({
                  type: 'success',
                  message: '处理成功 '
                });
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
          outImg(){
            this.$message({
              message: '上传图片超出数量限制',
              type: 'warning',
              duration:1000
            });
          },
          deleteOne(v){
            this.brands.splice(v,1);
          },
          /*添加更多*/
          addMore(){
            this.brands.push(this.brand_one);
            this.form.brands.push(this.brand_one)
          }
        },
        created() {

        },
      mounted(){
        window.addEventListener('scroll',this.handleScroll);
        if(this.$route.query.CTid){
          this.getCategorybrands(this.$route.query.CTid);
          this.form.CTid = this.$route.query.CTid;
        }
      },
    }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/_variate";
  @import "../../common/css/index";
  .m-input-l{
    width: 4.8rem;
  }
  .m-input-m{
    width: 2.8rem;
  }
  .m-input-s{
    width: 1.8rem;
  }
  .m-label{
    width: 1.2rem;
    text-align: right;
    float: left;
    font-size: 14px;
    color: #606266;
    line-height: 40px;
    padding: 0 12px 0 0;
    -webkit-box-sizing: border-box;
    box-sizing: border-box;
  }
  .m-switch-label{
    color: #606266;
  }
  .m-other{
    .m-input-s{
      margin-left: 0.1rem;
    }
  }
  .m-img-p{
    color: @greyColor;
    font-size: 0.12rem;
  }
  .m-link{
    color: @green;
    cursor: pointer;
  }
  .m-look-more{
    font-size: 0.12rem;
    color: @green;
    cursor: pointer;
    margin-top: 0.1rem;
  }
  .m-delete{
    color: @greyColor;
    margin-left: 0.4rem;
    cursor: pointer;
  }
  .m-goodsImported-content{
    background-color: #fff;
    font-size: 0.14rem;
    .m-edit-btn{
      padding: 0.1rem 0.4rem;
      text-align: right;
      color: @greyColor;
      font-size: 0.14rem;
      cursor: pointer;
    }
    .m-one-part{
      h3{
        background-color: #c8c9c9;
        padding: 0.14rem 0.4rem;
        font-weight: 600;
        margin-bottom: 0.2rem;
      }
      .m-alert{
        font-size: 0.12rem;
        color: @greyColor;
        line-height: 0.18rem;
      }
      .m-check-content{
        font-size: 0.12rem;
        color: @greyColor;
        line-height: 0.18rem;
      }
      .m-select-box{
        p.m-alert{
          line-height: 0.38rem;
        }
        .m-selects{
          width: 8.5rem;
          padding: 0.2rem 0;
          background-color: #eeeeee;
          display: flex;
          flex-flow: row;
          align-items: center;
          flex-wrap: wrap;
          .m-form-item{
            margin-bottom: 0.15rem;
            &:nth-child(even){
              margin-left: 0.8rem;
            }
          }
          .m-img-l{
            font-size: 0.14rem;
            color: @green;
          }
        }
      }
      .m-product-style{
        .m-product{
          display: flex;
          flex-flow: row;
          align-items: center;
          .m-product-input{
            display: flex;
            flex-flow: column;
            margin-right: 0.2rem;
            margin-bottom: 0.1rem;
            .m-input-m{
              margin-top: 0.1rem;
            }
          }

        }
        .m-img-label{
          display: inline-block;
          width: 0.5rem;
          text-align: right;
          color: @greyColor;
        }
        .m-add-more{
          font-size: 0.12rem;
          color: @green;
          padding-left: 0.8rem;
          cursor: pointer;
        }
      }
    }
    .m-goodsImported-foot{
      margin: 1rem 0.5rem 0;
      border-top: 1px solid @borderColor;
      height: 2rem;
      .flex-row(space-around);
      .m-foot-btn{
        display: block;
        width: 2rem;
        height: 0.5rem;
        line-height: 0.5rem;
        color: #fff;
        text-align: center;
        font-size: 0.18rem;
        border-radius: 5px;
        background-color: @btnActiveColor;
        cursor: pointer;
        border: 1px solid @btnActiveColor;
      }
    }
   }
  .m-right-side{
    position: fixed;
    right: 0.4rem;
    top: 50%;
    font-size: 0.12rem;
    .m-step-box{
      width: 1rem;
      ul{
        li{
          .flex-row(flex-start);
          a{
            .flex-row(flex-start);
          }
          span{
            display: block;
            color: @greyColor;
            cursor: pointer;
            &.circle{
              width: 0.15rem;
              height: 0.15rem;
              border-radius: 50%;
              border: 1px solid @borderColor;
              background-color: @borderColor;
              margin-right: 0.1rem;

              &.m-both-ends{
                background-color: #fff;
                cursor: inherit;
              }
              &.active{
                background-color: @btnActiveColor;
              }
            }
            &.line{
              width: 0.15rem;
              text-align: center;
              color: @borderColor;
              line-height: 0.15rem;
            }

          }
        }
      }
    }
    .m-side-btn{
      text-align: center;
      span.m-btn{
        display: inline-block;
        width: 0.8rem;
        height: 0.3rem;
        line-height: 0.3rem;
        background-color: @btnActiveColor;
        color: #fff;
        border-radius: 5px ;
        margin-top: 0.2rem;
        cursor: pointer;
      }
    }
  }
</style>
