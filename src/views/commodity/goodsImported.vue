<template>
<div>
  <el-form ref="form" :model="form" label-width="1.2rem">
    <page-title :title="name" @freshClick="freshClick"></page-title>
    <div class="m-goodsImported-content">
      <div class="m-edit-btn">
        <span>-编辑-</span>
      </div>
      <div class="m-one-part">
        <h3>基本信息</h3>
        <el-form-item label="活动名称:" :rules="[{ required: true, message: '年龄不能为空'},{ type: 'number', message: '年龄必须为数字值'}]">
          <el-input v-model="form.name" class="m-input-l" ></el-input>
        </el-form-item>
        <el-form-item label="活动名称:" :rules="[{ required: true, message: '年龄不能为空'}, { type: 'number', message: '年龄必须为数字值'}]">
          <el-input v-model="form.name" class="m-input-l" ></el-input>
          <p class="m-alert">建议描述文字在36字以内</p>
        </el-form-item>
        <el-form-item label="活动名称:" :rules="[{ required: true}]">
          <div class="m-select-box">
            <p class="m-alert">错误填写商品属性，可能会引起商品下架或搜索流量减少，影响您的正常销售，请认真准确填写！</p>
            <div class="m-selects">
              <el-form-item label="活动名称名:" class="m-form-item" :rules="[{ required: false}]">
                <el-input v-model="form.select" class="m-input-m" ></el-input>
              </el-form-item>
              <el-form-item label="姓名：" class="m-form-item" :rules="[{ required: false}]">
                <el-select v-model="form.select" class="m-input-m" >
                  <el-option label="区域一" value="shanghai"></el-option>
                  <el-option label="区域二" value="beijing"></el-option>
                </el-select>
              </el-form-item>
              <el-form-item label="活动名称名:" class="m-form-item" :rules="[{ required: false}]">
                <el-input v-model="form.select" class="m-input-m" ></el-input>
              </el-form-item>
              <el-form-item label="姓名：" class="m-form-item" :rules="[{ required: false}]">
                <el-select v-model="form.select" class="m-input-m" >
                  <el-option label="区域一" value="shanghai"></el-option>
                  <el-option label="区域二" value="beijing"></el-option>
                </el-select>
              </el-form-item>
            </div>
          </div>
        </el-form-item>
        <el-form-item label="活动名称:" :rules="[{ required: true, message: '年龄不能为空'},{ type: 'number', message: '年龄必须为数字值'}]">
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
        </el-form-item>
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
              dialogVisible: false
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
          }
        },
        created() {

        }
    }
</script>
<style lang="less" rel="stylesheet/less" scoped>
  @import "../../common/css/_variate";
.m-input-l{
  width: 4.8rem;
}
  .m-input-m{
    width: 1.9rem;
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
      p.m-alert{
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
    }
   }
</style>
