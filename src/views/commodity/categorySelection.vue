<template>
  <div>
    <el-form ref="form" :model="form" label-width="1.2rem">
      <page-title :title="name" @freshClick="freshClick"></page-title>
      <div class="m-goodsImported-content">
        <div class="m-edit-btn">
          <span>-编辑-</span>
        </div>
        <div class="m-one-part">
          <h3>类目选择</h3>
          <el-form-item label="类目搜索:" >
              <el-select v-model="form.CTid" filterable remote :remote-method="productBlur" class="m-input-s" >
                <el-option
                  v-for="(items,index) in product_list"
                  :key="index"
                  :label="items.CTname"
                  :value="items.CTid"></el-option>
              </el-select>
            <span class="m-btn" @click="search">搜索</span>
          </el-form-item>
          <!--<el-form-item label="快速选择:" :rules="[{ required: true, message: '年龄不能为空'}, { type: 'number', message: '年龄必须为数字值'}]">-->
            <!--<el-select v-model="form.select" class="m-input-l">-->
              <!--<el-option label="区域一" value="shanghai"></el-option>-->
              <!--<el-option label="区域二" value="beijing"></el-option>-->
            <!--</el-select>-->
          <!--</el-form-item>-->
          <el-form-item label="商品类目:" :rules="[{ required: true}]">
            <div class="m-select-box">
              <p class="m-alert">错误填写商品属性，可能会引起商品下架或搜索流量减少，影响您的正常销售，请认真准确填写！</p>
              <div class="m-selects">
                <div class="m-left-right"><span class="m-btn-img m-left-btn-img" :class="scroll_index>0? 'active':''" @click="scroll(-1)"></span></div>
                <div class="m-category-content">
                  <div id="m-scroll">
                      <div class="m-one-category" v-for="(items,index) in category_list" :key="Math.random()">
                        <div class="m-search-box">
                          <span class="icon icon-search"></span>
                          <input type="text" v-model="category_input[index]" placeholder=""  @change="changeInput(index)">
                        </div>
                        <div class="m-classify">
                          <ul>
                            <template v-for="(item,i) in items">
                              <!--<template v-for="(itemss,i) in item">-->
                                <li :class="select_category[index] && select_category[index].CTid == item.CTid? 'active':''"  :key="Math.random()" @click="selectCategory(item,index)">
                                  <span>{{item.CTname}}</span>
                                  <i class="el-icon-arrow-right"></i>
                                </li>
                              <!--</template>-->
                            </template>
                          </ul>
                        </div>
                      </div>
                  </div>
                </div>
                <div class="m-left-right"><span class="m-btn-img m-right-btn-img" :class="category_list.length > 3 ? 'active':''" @click="scroll(1)"></span></div>
              </div>
              <div class="m-now-select">
                <p>当前选择类目：
                 <template v-for="(item,index) in select_category">
                   <span>{{item.CTname}} <i v-if="index+1 < select_category.length"> > </i></span>
                 </template>
                </p>
              </div>
              <div class="m-rule-box">
                <h3>规则</h3>
                <div class="m-rule">
                  <p><span>发布须知</span>：平台禁止发布侵犯他人知识产权的商品，请确认商品符合知识产权保护的规定！</p>
                </div>
              </div>
              <div class="m-check">
                <el-checkbox v-model="checked">我已阅读以上规则</el-checkbox>
              </div>
            </div>
          </el-form-item>
        </div>
        <div class="m-goodsImported-foot">
          <span class="m-foot-btn" @click="nextClick">下一步</span>
        </div>
      </div>
    </el-form>
  </div>

</template>
<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  import api from '../../api/api';
  import { Message} from 'element-ui';
  import axios from 'axios';
  export default {
    data() {
      return {
        name:'商品发布',
        form:{
          CTid:''
        },
        checked:true,
        scroll_index:0,
        product_list:[],
        category_list:[],
        select_category:[],
        select_category1:[
          {
            CTfromid: "0",
            CTid: "1",
            CTname: "百货食品"
          },
          {
            CTfromid: "1",
            CTid: "4",
            CTname: "生鲜"
          },
          {
            CTfromid: "2",
            CTid: "10",
            CTname: "小龙虾"
          }
        ],
        category_input:[]
      }
    },
    components:{
      pageTitle
    },
    mounted(){
      if(this.$route.query.CTid){
        this.getProductSelect(this.$route.query.CTid);
      }else{
        this.getChildCategory('',0);
      }
      this.getProductList('')

      //
    },
    methods: {
      freshClick(){
        console.log('fresh');
      },
      /*搜索*/
      search(){
        let that = this;
        if(!that.form.CTid){
          return false;
        }else{
          that.getProductSelect(that.form.CTid)
        }
      },
      /*下拉框模糊搜索*/
      productBlur(e){
        this.getProductList(e)
      },
      /*文本框模糊搜索*/
      changeInput(i){
        console.log(i)
        if(i == 0){
          this.getChildCategory('',0,this.category_input[i]);
        }else{
          this.getChildCategory(this.select_category[i-1].CTid,i,this.category_input[i]);
        }
      },
      /*获取商品*/
      getProductList(name){
        let that = this;
        that.product_list = [];
        let _arr = that.product_list;
        axios.get(api.get_category_by_prname ,{params:{
            // token:this.$store.state.token
            token:localStorage.getItem('token'),
            PRname:name
          }}).then(res => {
          if(res.data.status == 200){
            _arr = res.data.data ;
            that.product_list = [].concat(_arr);
          }else{
            this.$message.error(res.data.message);
          }
        },error => {
          this.$message.error(error.data.message);
        })
      },
      /*获取CTid对应商品*/
      getProductSelect(id){
        let that = this;
        that.select_category = [];
        let _arr = that.select_category;
        axios.get(api.get_ctlist_by_ctid ,{params:{
            // token:this.$store.state.token
            token:localStorage.getItem('token'),
            CTid:id
          }}).then(res => {
          if(res.data.status == 200){
            _arr = res.data.data ;
            that.select_category = [].concat(_arr);
            that.getCategory()
          }else{
            this.$message.error(res.data.message);
          }
        },error => {
          this.$message.error(error.data.message);
        })
      },
      /*获取类目*/
      getChildCategory(id,i,code){
        let that = this;
        let _arr = that.category_list;
        axios.get(api.get_child_category,{params:{
            // token:this.$store.state.token
            token:localStorage.getItem('token'),
            CTid:id,
            category_filter:code
          }}).then(res => {
          if(res.data.status == 200){
              if(res.data.data.length < 1 && !code ){
                that.$message({
                  message:'已经达到最后一层',
                  type:'warning'
                })
              }else{
                  _arr[i] = res.data.data ;
                that.category_list = [].concat(_arr);
              }


          }else{
            this.$message.error(res.data.message);
          }
        },error => {
          this.$message.error(error.data.message);
        })
      },
      /*获取子类目*/
      selectCategory(v,i){
        let _arr = this.select_category;
         _arr[i] = v;
         for(let j=0;j<_arr.length;j++){
           if(j > i){
             _arr = _arr.slice(0,j)
           }
         }
        this.select_category = [].concat(_arr);
        this.getChildCategory(v.CTid,i+1);
      },
      /*带参获取类目信息*/
      getCategory(){
        for(let i=0;i< this.select_category.length;i++){
          if(i ==0 ){
            this.getChildCategory('',0);
          }else{
            this.getChildCategory(this.select_category[i-1].CTid,i);
          }
        }
      },
      /*类目滚动*/
      sideClick(v){
        this.linkTo = v;
      },
      /*类目左右滚动*/
      scroll(v){
        let _scroll = document.getElementById('m-scroll');
        if(v == -1 && this.scroll_index == 0){
          return false;
        }
        if(v == 1 && (this.scroll_index == this.category_list.length || this.category_list.length <=3)){
          return false;
        }
        //待判断右终点
        this.scroll_index = this.scroll_index + Number(v);
        _scroll.style.marginLeft = this.scroll_index * -2.08 +'rem';
      },
      /*下一步*/
      nextClick(){
        if(!this.checked){
          this.$message.error('请先阅读以上规则');
          return false;
        }
        if(this.select_category.length < this.category_list.length){
          this.$message.error('请先选择具体类目');
          return false;
        }
        this.$router.push({path:'/commodity/goodsImported',query:{CTid:this.select_category[this.select_category.length -1].CTid}});
      }
    },
    created() {

    }
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
  .m-btn{
    display: inline-block;
    width: 0.8rem;
    height: 0.32rem;
    text-align: center;
    line-height: 0.32rem;
    background-color: @btnActiveColor;
    color: #fff;
    border-radius: 5px;
    margin-left: 0.1rem;
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
        width: 7.2rem;
        p.m-alert{
          line-height: 0.38rem;
        }
        .m-selects{
          padding: 0.2rem;
          height: 3.2rem;
          background-color: #eeeeee;
          display: flex;
          flex-flow: row;
          align-items: center;
          border-radius: 5px;
          .m-left-right{
            width: 0.2rem;
            height: 100%;
            display: flex;
            align-items: center;
            span{
              display: block;
              width: 0.16rem;
              height: 0.6rem;
              background: url("../../common/images/icon-left.png");
              background-size: 100% 100%;
              cursor: not-allowed;
              &.m-left-btn-img{
                &.active{
                  background: url("../../common/images/icon-left-active.png");
                  background-size: 100% 100%;
                  cursor: pointer;
                }
              }
              &.m-right-btn-img{
                background: url("../../common/images/icon-right.png");
                background-size: 100% 100%;
                &.active{
                  background: url("../../common/images/icon-right-active.png");
                  background-size: 100% 100%;
                  cursor: pointer;
                }
              }
            }
          }
          .m-category-content{
            width: 6.2rem;
            height: 100%;
            overflow: hidden;
            #m-scroll{
              margin-left: 0;
              -webkit-transition: margin-left 0.28s;
              transition: margin-left 0.28s;
              .flex-row(flex-start);
            }
            .m-one-category{
              width: 1.8rem;
              height: 90%;
              border: 1px solid @sidebarChildColor;
              border-radius: 5px;
              background-color: #fff;
              text-align: center;
              padding: 0.1rem 0.08rem 0;
              margin-right: 0.1rem;
              .m-search-box{
                width: 1.80rem;
                height: 0.27rem;
                line-height: 0.27rem;
                font-size: 0.12rem;
                border: 1px solid @mainColor;
                position: relative;
                border-radius: 5px;
                .icon-search{
                  width: 0.18rem;
                  height: 0.18rem;
                  position: absolute;
                  top: 0.05rem;
                  left: 0.1rem;
                  background: url("../../common/images/icon-search.png");
                  background-size: 100% 100%;
                }
                input{
                  border: none;
                  height: 0.27rem;
                  width: 1.4rem;
                  padding-left: 0.4rem;
                  &:focus{
                    border: none;
                    outline-offset: 0;
                    outline-color:transparent;
                  }
                }
              }
              .m-classify{
                height: 2.65rem;
                margin-top: 0.1rem;
                overflow-y: scroll;
                ul{
                  li{
                    .flex-row(space-between);
                    padding: 0 0.1rem 0.1rem;
                    color: @greyColor;
                    cursor: pointer;
                    &.active{
                      color: @sidebarChildColor;
                    }
                    span{
                      display: block;
                      line-height: 0.2rem;
                    }
                  }
                }
              }
            }
          }
        }
        .m-now-select{
          padding: 0.05rem 0.2rem 0.15rem;
          background-color: #eeeeee;
          margin: 0.1rem 0;
          border-radius: 5px;
          span{
            font-size: 0.12rem;
            color: @greyColor;
          }
        }
        .m-rule-box{
          padding: 0 0.2rem 0.2rem;
          border: 1px solid @sidebarChildColor;
          border-radius: 5px;
          h3{
            background-color: #fff;
            border-bottom: 1px solid @borderColor;
            padding:0 0 0 0.1rem;
            text-align: center;
          }
          .m-rule{
            height: 1rem;
            overflow-y: auto;
            color: @greyColor;
            span{
              color: #000;
            }
          }
        }
        .m-check{
          text-align: right;
        }
      }
    }
    .m-goodsImported-foot{
      margin: 0 0.5rem 0;
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
      }
    }
  }
  /*滚动条样式*/
  .m-classify::-webkit-scrollbar {/*滚动条整体样式*/
    width: 5px;     /*高宽分别对应横竖滚动条的尺寸*/
    height: 5px;
  }
  .m-classify::-webkit-scrollbar-thumb {/*滚动条里面小方块*/
    border-radius: 10px;
    -webkit-box-shadow: inset 0 0 5px @sidebarChildColor;
    background: @sidebarChildColor;
  }
  .m-classify::-webkit-scrollbar-track {/*滚动条里面轨道*/
    -webkit-box-shadow: inset 0 0 5px @scrollBgColor;
    border-radius: 10px;
    background:@scrollBgColor;
  }
  /*滚动条样式*/
  .m-rule::-webkit-scrollbar {/*滚动条整体样式*/
    width: 5px;     /*高宽分别对应横竖滚动条的尺寸*/
    height: 5px;
  }
  .m-rule::-webkit-scrollbar-thumb {/*滚动条里面小方块*/
    border-radius: 10px;
    -webkit-box-shadow: inset 0 0 5px @sidebarChildColor;
    background: @sidebarChildColor;
  }
  .m-rule::-webkit-scrollbar-track {/*滚动条里面轨道*/
    -webkit-box-shadow: inset 0 0 5px @scrollBgColor;
    border-radius: 10px;
    background:@scrollBgColor;
  }
</style>
