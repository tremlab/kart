import React from 'react';
import $ from 'jquery';
import Kart from './Kart.jsx';

class UserInput extends React.Component {
	constructor(props) {
		super(props);
		this.state = {
			userInput: '',
			kart: []
		};
		this.handleInputAdd = this.handleInputAdd.bind(this);
		this.handleInputChange = this.handleInputChange.bind(this);
	}
	handleInputAdd(event) {
		event.preventDefault();
		console.log('adding...')
		const uInput = this.state.userInput

		if (uInput) {
			$.post(window.location.href + 'kartItem', {"userInput": uInput}, (data) => {
					this.setState({ kart: data })
			  });

			this.setState({
				userInput: ''
			});
		}
	}
	handleInputChange(event) {
		const value = event.target.value;
		this.setState({
			userInput: value
		});
		// get suggestions and display
	}
	render() {
		return (
			<div>
				<form className="Form">
					<input placeholder="start typing...." value={this.state.userInput} onChange={this.handleInputChange} />
					<button onClick={this.handleInputAdd}>Add</button>
				</form>
				<Kart kart={this.state.kart}/>
			</div>
		);
	}
}

export default UserInput;
