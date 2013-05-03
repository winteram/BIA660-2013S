<%@ Page Title="BIA660-NYC311" Language="C#" MasterPageFile="Site.master" AutoEventWireup="true"
    CodeFile="Default.aspx.cs" Inherits="_Default" %>

<%@ Register assembly="System.Web.DataVisualization, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35" namespace="System.Web.UI.DataVisualization.Charting" tagprefix="asp" %>

<asp:Content ID="HeaderContent" runat="server" ContentPlaceHolderID="HeadContent">
    <style type="text/css">
        .style2
        {
            width: 424px;
            margin-left: 120px;
        }
        .style3
        {
            width: 1627px;
        }
        .style4
        {
            width: 402px;
            margin-left: 120px;
        }
        .style5
        {
            width: 263px;
            margin-left: 120px;
        }
        .style6
        {
            width: 263px;
        }
    </style>
</asp:Content>
<asp:Content ID="BodyContent" runat="server" ContentPlaceHolderID="MainContent">
    <h2>
        New York City Resident 'Quality of Life' Complaints to 311  
    </h2>
    <p>
        Investigate 2 neighborhoods in NYC for a selected month.
    </p>
    
        <table style="width: 100%;">
            <tr>
                <td class="style4">
                    <asp:ListBox ID="ListBox1" runat="server" 
                        onselectedindexchanged="ListBox1_SelectedIndexChanged" Width="247px">
                    </asp:ListBox>
                </td>
                <td class="style2">
                    <asp:ListBox ID="ListBox2" runat="server" 
                        onselectedindexchanged="ListBox2_SelectedIndexChanged" Width="247px"> 
                    </asp:ListBox>
                </td>
                <td class="style5">
                    <div>&nbsp;&nbsp;&nbsp;&nbsp;
                    <asp:Button ID="Button1" runat="server" onclick="Button1_Click" 
                        Text="Refresh" style="margin-left: 0px" />
                        <br />
                        <br />
                        Date Selection</div>
                    <asp:DropDownList ID="DropDownList1" runat="server">
                        <asp:ListItem Value="01">Jan</asp:ListItem>
                        <asp:ListItem Value="02">Feb</asp:ListItem>
                        <asp:ListItem Value="03">Mar</asp:ListItem>
                        <asp:ListItem Value="04">Apr</asp:ListItem>
                        <asp:ListItem Value="05">May</asp:ListItem>
                        <asp:ListItem Value="06">Jun</asp:ListItem>
                        <asp:ListItem Value="07">Jul</asp:ListItem>
                        <asp:ListItem Value="08">Aug</asp:ListItem>
                        <asp:ListItem Value="09">Sep</asp:ListItem>
                        <asp:ListItem Value="10">Oct</asp:ListItem>
                        <asp:ListItem Value="11">Nov</asp:ListItem>
                        <asp:ListItem Value="12">Dec</asp:ListItem>
                    </asp:DropDownList>
                    <asp:DropDownList ID="DropDownList2" runat="server">
                        <asp:ListItem>2013</asp:ListItem>
                        <asp:ListItem>2012</asp:ListItem>
                    </asp:DropDownList>
&nbsp;&nbsp;&nbsp;&nbsp;
                </td>
                <td class="style4">
                    &nbsp;</td>
            </tr>
            <tr>
                <td>
                    <asp:CheckBox ID="CheckBox1" runat="server" 
                        Text="Remove Housing/Landlord Issues" />
                </td>

                <td>
                    <asp:CheckBox ID="CheckBox2" runat="server" 
                        Text="Remove Housing/Landlord Issues" />
                </td>

                <td class="style6">
                    <asp:TextBox ID="TextBox1" runat="server" Width="43px" Height="16px" 
                        Visible="False">1/1/2013</asp:TextBox>
                </td>
            </tr>

        </table>

        <table style="width: 100%;">
            <tr style="width:70%;">
                <td class="style4" align="center">
                    &nbsp;
                    <asp:Chart ID="Chart1" runat="server" 
                            Width="600px" 
                            ImageLocation="./App_Data/Chart1" Height="325px">
                        <series>
                            <asp:Series Name="Series1" XValueMember="complaint" 
                                YValueMembers="CT" ChartType="Bar">
                            </asp:Series>
                        </series>
                        <chartareas>
                            <asp:ChartArea Name="ChartArea1">
                                <AxisY TitleFont="Microsoft Sans Serif, 6pt">
                                </AxisY>
                                <AxisX IntervalAutoMode="VariableCount" TitleFont="Microsoft Sans Serif, 6pt">
                                    <LabelStyle Interval="Auto" />
                                </AxisX>
                            </asp:ChartArea>
                        </chartareas>
                    </asp:Chart>
                </td>

                <td class="style3" align="left" valign="top">
                    <h2><asp:Label ID="Label1" runat="server" Text="Upper East Side"></asp:Label></h2>
                    <asp:GridView ID="GridView2" runat="server" AutoGenerateColumns="False" 
                        Width="300px" CellPadding="4" 
                        ForeColor="#333333" GridLines="None" 
                        onselectedindexchanged="GridView2_SelectedIndexChanged" 
                        BorderColor="#6600FF" BorderStyle="Solid" BorderWidth="1px">
                        <AlternatingRowStyle BackColor="White" ForeColor="#284775" />
                        <Columns>
                            <asp:BoundField DataField="ZipCode" HeaderText="ZipCode" 
                                SortExpression="ZipCode" />
                            <asp:BoundField DataField="AvgIncome" DataFormatString="{0:C}" 
                                HeaderText="Avg Income" SortExpression="AvgIncome" />
                            <asp:BoundField DataField="BelowPovertyLine" DataFormatString="{0:P2}" 
                                HeaderText="Below Poverty Line" SortExpression="BelowPovertyLine" />
                            <asp:BoundField DataField="Population" HeaderText="Population" 
                                SortExpression="Population" /> 
                        </Columns>
                        <EditRowStyle BackColor="#999999" />
                        <FooterStyle BackColor="#5D7B9D" Font-Bold="True" ForeColor="White" />
                        <HeaderStyle BackColor="#5D7B9D" Font-Bold="True" ForeColor="White" />
                        <PagerStyle BackColor="#284775" ForeColor="White" HorizontalAlign="Center" />
                        <RowStyle BackColor="#F7F6F3" ForeColor="#333333" HorizontalAlign="Right" />
                        <SelectedRowStyle BackColor="#E2DED6" Font-Bold="True" ForeColor="#333333" 
                            HorizontalAlign="Right" />
                        <SortedAscendingCellStyle BackColor="#E9E7E2" />
                        <SortedAscendingHeaderStyle BackColor="#506C8C" />
                        <SortedDescendingCellStyle BackColor="#FFFDF8" />
                        <SortedDescendingHeaderStyle BackColor="#6F8DAE" />
                    </asp:GridView>
                </td>
            </tr>
            <tr>
                <td class="style4">
                    <asp:Chart ID="Chart2" runat="server" 
                            Width="600px" 
                            ImageLocation="./App_Data/Chart2" Height="325px">
                        <series>
                            <asp:Series Name="Series1" XValueMember="complaint" 
                                YValueMembers="CT" ChartType="Bar">
                            </asp:Series>
                        </series>
                        <chartareas>
                            <asp:ChartArea Name="ChartArea1">
                                <AxisY TitleFont="Microsoft Sans Serif, 6pt">
                                </AxisY>
                                <AxisX IntervalAutoMode="VariableCount" TitleFont="Microsoft Sans Serif, 6pt">
                                    <LabelStyle Interval="Auto" />
                                </AxisX>
                            </asp:ChartArea>
                        </chartareas>
                    </asp:Chart>
                </td>

                <td class="style3" align="left" valign="top">
                    <h2><asp:Label ID="Label2" runat="server" Text="Upper East Side"></asp:Label></h2>
                    <asp:GridView ID="GridView1" runat="server" AutoGenerateColumns="False" 
                        onselectedindexchanged="GridView1_SelectedIndexChanged" Width="300px" 
                        CellPadding="4" ForeColor="#333333" GridLines="None" 
                        style="text-align: center" BorderColor="#6600FF" BorderStyle="Solid" 
                        BorderWidth="1px">
                        <AlternatingRowStyle BackColor="White" ForeColor="#284775" />
                        <Columns>
                            <asp:BoundField DataField="ZipCode" HeaderText="ZipCode" 
                                SortExpression="ZipCode" />
                            <asp:BoundField DataField="AvgIncome" DataFormatString="{0:C}" 
                                HeaderText="Avg Income" SortExpression="AvgIncome" />
                            <asp:BoundField DataField="BelowPovertyLine" DataFormatString="{0:P2}" 
                                HeaderText="Below Poverty Line" SortExpression="BelowPovertyLine" />
                            <asp:BoundField DataField="Population" HeaderText="Population" 
                                SortExpression="Population" /> 
                        </Columns>
                        <EditRowStyle BackColor="#999999" />
                        <FooterStyle BackColor="#5D7B9D" Font-Bold="True" ForeColor="White" />
                        <HeaderStyle BackColor="#5D7B9D" Font-Bold="True" ForeColor="White" />
                        <PagerStyle BackColor="#284775" ForeColor="White" HorizontalAlign="Center" />
                        <RowStyle BackColor="#F7F6F3" ForeColor="#333333" HorizontalAlign="Right" />
                        <SelectedRowStyle BackColor="#E2DED6" Font-Bold="True" ForeColor="#333333" 
                            HorizontalAlign="Right" />
                        <SortedAscendingCellStyle BackColor="#E9E7E2" />
                        <SortedAscendingHeaderStyle BackColor="#506C8C" />
                        <SortedDescendingCellStyle BackColor="#FFFDF8" />
                        <SortedDescendingHeaderStyle BackColor="#6F8DAE" />
                    </asp:GridView>
                </td>
            </tr>
        </table>

    <p>
        &nbsp;</p>
</asp:Content>
