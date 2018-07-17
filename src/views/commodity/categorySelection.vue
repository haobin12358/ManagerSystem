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
          <el-form-item label="类目搜索:" :rules="[{ required: true, message: '年龄不能为空'},{ type: 'number', message: '年龄必须为数字值'}]">
            <el-input v-model="form.name" class="m-input-l" ></el-input>
            <span class="m-btn">搜索</span>
          </el-form-item>
          <el-form-item label="快速选择:" :rules="[{ required: true, message: '年龄不能为空'}, { type: 'number', message: '年龄必须为数字值'}]">
            <el-select v-model="form.select" class="m-input-l">
              <el-option label="区域一" value="shanghai"></el-option>
              <el-option label="区域二" value="beijing"></el-option>
            </el-select>
          </el-form-item>
          <el-form-item label="商品类目:" :rules="[{ required: true}]">
            <div class="m-select-box">
              <p class="m-alert">错误填写商品属性，可能会引起商品下架或搜索流量减少，影响您的正常销售，请认真准确填写！</p>
              <div class="m-selects">
                <div class="m-left-right"><span class="m-btn-img m-left-btn-img" @click="scroll(-1)"></span></div>
                <div class="m-category-content">
                  <div id="m-scroll">
                    <div class="m-one-category">
                      <div class="m-search-box">
                        <span class="icon icon-search"></span>
                        <input type="text" placeholder="">
                      </div>
                      <div class="m-classify">
                        <ul>
                          <li>
                            <span>游戏话费</span>
                            <i class="el-icon-arrow-right"></i>
                          </li>
                          <li>
                            <span>游戏话费</span>
                            <i class="el-icon-arrow-right"></i>
                          </li>
                          <li>
                            <span>游戏话费</span>
                            <i class="el-icon-arrow-right"></i>
                          </li>
                        </ul>
                      </div>
                    </div>
                    <div class="m-one-category">
                      <div class="m-search-box">
                        <span class="icon icon-search"></span>
                        <input type="text" placeholder="">
                      </div>
                      <div class="m-classify">
                        <ul>
                          <li>
                            <span>游戏话费</span>
                            <i class="el-icon-arrow-right"></i>
                          </li>
                          <li>
                            <span>游戏话费</span>
                            <i class="el-icon-arrow-right"></i>
                          </li>
                        </ul>
                      </div>
                    </div>
                    <div class="m-one-category">
                      <div class="m-search-box">
                        <span class="icon icon-search"></span>
                        <input type="text" placeholder="">
                      </div>
                      <div class="m-classify">
                        <ul>
                          <li>
                            <span>游戏话费</span>
                            <i class="el-icon-arrow-right"></i>
                          </li>
                          <li>
                            <span>游戏话费</span>
                            <i class="el-icon-arrow-right"></i>
                          </li>
                          <li>
                            <span>梳子/便携用镜</span>
                            <i class="el-icon-arrow-right"></i>
                          </li>
                        </ul>
                      </div>
                    </div>
                    <div class="m-one-category">
                      <div class="m-search-box">
                        <span class="icon icon-search"></span>
                        <input type="text" placeholder="">
                      </div>
                      <div class="m-classify">
                        <ul>
                          <li>
                            <span>游戏话费</span>
                            <i class="el-icon-arrow-right"></i>
                          </li>
                          <li>
                            <span>游戏话费</span>
                            <i class="el-icon-arrow-right"></i>
                          </li>
                          <li>
                            <span>梳子/便携用镜</span>
                            <i class="el-icon-arrow-right"></i>
                          </li>
                        </ul>
                      </div>
                    </div>
                  </div>
                </div>
                <div class="m-left-right"><span class="m-btn-img m-right-btn-img active" @click="scroll(1)"></span></div>
              </div>
              <div class="m-now-select">
                <p>当前选择类目：<span >家庭/个人清洁工具 > 个人洗护清洁用具 > 梳子/便携用镜 > 镜梳套装 > 礼盒/套装</span></p>
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
          <router-link to="/commodity/goodsImported">
          <span class="m-foot-btn">下一步</span>
          </router-link>
        </div>
      </div>
    </el-form>
  </div>

</template>
<script type="text/ecmascript-6">
  import pageTitle from '../../components/common/title';
  export default {
    data() {
      return {
        name:'商品发布',
        form:{
          name:'',
          select:''
        },
        dialogImageUrl: '',
        dialogVisible: false,
        checked:true,
        radio:0,
        linkTo:'basicInfo',
        scroll_index:0
      }
    },
    components:{
      pageTitle
    },
    methods: {
      freshClick(){
        console.log('fresh');
      },
      handleRemove(file, fileList) {
        console.log(file, fileList);
      },
      handlePictureCardPreview(file) {
        this.dialogImageUrl = file.url;
        this.dialogVisible = true;
      },
      sideClick(v){
        this.linkTo = v;
      },
      scroll(v){

        let _scroll = document.getElementById('m-scroll');
        if(v == -1 && this.scroll_index == 0){
          return false;
        }
        //待判断右终点
        this.scroll_index = this.scroll_index + Number(v);
        _scroll.style.marginLeft = this.scroll_index * -2.06 +'rem';
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
              cursor: pointer;
              &.m-left-btn-img{
                &.active{
                  background: url("../../common/images/icon-left-active.png");
                  background-size: 100% 100%;
                }
              }
              &.m-right-btn-img{
                background: url("../../common/images/icon-right.png");
                background-size: 100% 100%;
                &.active{
                  background: url("../../common/images/icon-right-active.png");
                  background-size: 100% 100%;
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
